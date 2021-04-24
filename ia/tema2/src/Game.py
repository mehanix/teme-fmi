import pygame
import copy

from collections import defaultdict


class Config:
    """Aici tin setari folosite pe perioada intreaga a jocului pentru a le putea accesa usor cand am nevoie de ele.
    """

    @classmethod
    def set(cls,tip_joc,dificultate, lat, lung):
        cls.tip_joc = tip_joc
        cls.dificultate = dificultate
        cls.latime_ecran = lat
        cls.lungime_ecran = lung + 40
        cls.ADANCIME_MAX = 1 + int(dificultate)
 
    @classmethod
    def set_ecran(cls,ecr):
        """Seteaza ecranul jocului

        Args:
            ecr (Surface): Ecranul pe care se va desena jocul
        """
        cls.ecran = ecr


class Celula:
    """O celula din tabla de joc.
    Contine atat rect-urile necesare pentru desenare cat si informatia din celula (ce laturi are completate)
    """
    grosimeZid=11 #numar impar
    culoareLinii=(62,53,54)
    culoarePuncte = (0,0,0)
    razaPuncte = 12
    afisImagini=True

    def __init__ (self, left, top, w, h):
        """Constructor pentru celula.

        Args:
            left (int): pozitia pe X
            top (int): pozitia pe Y
            w (int): latime
            h (int): lungime
        """
        self.fundalCelula=(255,255,255)
        self.dreptunghi=pygame.Rect(left, top, w, h)
        self.zid=[None,None,None,None]
        #zidurile vor fi pe pozitiile 0-sus, 1-dreapta, 2-jos, 3-stanga
        self.cod=0
        self.zid[0]=pygame.Rect(left,top-1-self.__class__.grosimeZid//2, w,self.__class__.grosimeZid)

        self.zid[1]=pygame.Rect(left+w-self.__class__.grosimeZid//2,top, self.__class__.grosimeZid, h)

        self.zid[2]=pygame.Rect(left,top+h-self.__class__.grosimeZid//2, w,self.__class__.grosimeZid)

        self.zid[3]=pygame.Rect(left-1-self.__class__.grosimeZid//2,top, self.__class__.grosimeZid,h)
 
        #0001 zid doar sus
        #0011 zid sus si dreapta etc

    def deseneaza(self):
        """Randeaza atat celula in sine cat si zidurile ei.
        """
        pygame.draw.rect(Config.ecran, self.fundalCelula, self.dreptunghi)
        masca=1
        for i in range(4):
            if self.cod & masca:
                if self.zid[i]:
                    pygame.draw.rect(Config.ecran, self.__class__.culoareLinii, self.zid[i])        
            masca*=2

                # top left
        
        pygame.draw.circle(Interfata.dotSurface,self.culoarePuncte,(self.dreptunghi.x,self.dreptunghi.y),self.razaPuncte)
        #top right
        pygame.draw.circle(Interfata.dotSurface,self.culoarePuncte,(self.dreptunghi.x,self.dreptunghi.y + self.dreptunghi.w),self.razaPuncte)
        pygame.draw.circle(Interfata.dotSurface,self.culoarePuncte,(self.dreptunghi.x+self.dreptunghi.h,self.dreptunghi.y + self.dreptunghi.w),self.razaPuncte)
        pygame.draw.circle(Interfata.dotSurface,self.culoarePuncte,(self.dreptunghi.x+self.dreptunghi.h,self.dreptunghi.y),self.razaPuncte)

    def exista_zid(self, i_zid):
        """Afla daca zidul i_zid a fost deja selectat de cineva.

        Args:
            i_zid (int): id-ul zidului

        Returns:
            bool: t/f daca a fost selectat sau nu
        """
        return self.cod & 2**i_zid

    def __repr__(self):
        return "Celula " + str(self.dreptunghi.x) + '  ' + str(self.dreptunghi.y)

class Interfata:
    """Tabla de joc, practic.
    Contine informatiile tablei de joc + se ocupa de desenarea ei.
    """

    # initializari
    culoareEcran=(210,205,201)
    JMIN = None #player
    JMAX = None #computer
    scor_maxim = 0

    def __init__(self, matr, nrLinii=3, nrColoane=3, capturaPlayer=None,capturaComputer=None):
        """Constructor tabla de joc.

        Args:
            matr ([[Celula]]): Tabla efectiva - poate fi pasata, sau daca e None, genereaza o tabla goala.
            nrLinii (int, optional): nr linii. Defaults to 3.
            nrColoane (int, optional): nr linii. Defaults to 3.
            capturaPlayer ([(int,int)], optional): Lista celulelor capturate de player. Defaults to None.
            capturaComputer ([(int,int)], optional): Lista celulelor capturate de player. Defaults to None.
        """
        self.ultima_mutare = None
        self.nrLinii=nrLinii
        self.nrColoane=nrColoane
        self.matrCelule=matr if matr is not None else [[Celula(left=col*(self.__class__.dimCelula+1)+30, top=lin*(self.__class__.dimCelula+1)+30, w=self.__class__.dimCelula, h=self.__class__.dimCelula) for col in range(nrColoane)] for lin in range(nrLinii) ]
        
        self.capturaPlayer = copy.deepcopy(capturaPlayer) if capturaPlayer is not None else []
        self.capturaComputer = copy.deepcopy(capturaComputer) if capturaComputer is not None else []

    @classmethod
    def getMatCoordZiduri(cls,matr):
        """Aici fac o precalculare pentru a incerca sa fac functia de generare succesori mai rapida.
        Ea original functiona in N^4, cu precalcularea asta am redus-o in n^2.
        Practic, creez un dictionar care mapeaza 1 zid la o lista de coordonate a celulelor afectate la click-ul pe zidul respectiv.

        Args:
            matr ([[Celula]]): Matrice de celule
        """
        cls.ziduri_dict = defaultdict(def_val)
        for il, linie in enumerate(matr):
            for ic, cel in enumerate(linie):                    
                for iz,zid in enumerate(cel.zid):
                    pos = zid.center
                    if zid.collidepoint(pos):
                        cls.ziduri_dict[pos].append((il,ic,iz))
        return 

    def marcheaza(self,simbol):
        """Cand se termina jocul, coloreaza patratelele castigatorului cu mov.

        Args:
            simbol (string): "X"sau "O"
        """

        winner = self.capturaPlayer if simbol == Interfata.JMIN else self.capturaComputer
        bkg_color = (167,89,179)
        for il, linie in enumerate(self.matrCelule):
            for ic, cel in enumerate(linie): 
                if (il,ic) in winner:
                    cel.fundalCelula = bkg_color
                    cel.deseneaza()
            


    def final(self):
        """Determina daca jocul s-a incheiat.
        Daca nr patratele total = nr patratele player + nr patratele computer, jocul e gata.

        Returns:
            string: Cine a castigat, sau remiza
        """
        nrPatrate = self.nrColoane * self.nrLinii
        scorPc = len(self.capturaComputer)
        scorPlayer = len(self.capturaPlayer)
        if nrPatrate == scorPc + scorPlayer:
            if scorPc == scorPlayer:
                return 'remiza'
            elif scorPc > scorPlayer:
                return Interfata.JMAX
            else:
                return Interfata.JMIN
        else:
            return False

    def deseneazaImag(self, imag, cel):
        """Deseneaza simbolul imag in celula cel.

        Args:
            imag ([image]): Imagine
            cel (Celula): Celula
        """
        Config.ecran.blit(imag,(cel.dreptunghi.left+self.__class__.paddingCelula,  cel.dreptunghi.top+self.__class__.paddingCelula))


    def deseneazaEcranJoc(self):
        """Deseneaza ecranul jocului si patratelele capturate.
        """
        Config.ecran.fill(self.__class__.culoareEcran)
        for il, linie in enumerate(self.matrCelule):
            for ic, cel in enumerate(linie):     
                cel.deseneaza() 
                if cel.cod == 15:
                    if (il,ic) in self.capturaPlayer:
                        self.deseneazaImag(self.img_player, cel)
                    else:
                        self.deseneazaImag(self.img_computer,cel)
                    # print("PLAYER",self.capturaPlayer)
                    # print("Computer",self.capturaComputer)
            

    def mutari(self,jucator):
        """Functie de generare a tuturor mutarilor posibile ale unui jucator.

        Args:
            jucator (JMIN sau JMAX): jucatorul care vrea sa faca mutarea

        Returns:
            (interfata, JMIN/JMAX): Tabla noua, respectiv al cui e randul in continuare (daca a capturat un patratel, isi pastreaza tura jucatorul curent)
        """
        l_mutari = []
        juc_opus = self.jucator_opus(jucator)

        #iterez prin toate zidurile
        # pt fiecare zid, iau celulele pe care selectarea lui le va afecta, daca acesta nu e deja selectat
        for lst in Interfata.ziduri_dict.values():
            celAfectate = []
            for (il,ic,iz) in lst:
                if not self.matrCelule[il][ic].exista_zid(iz):
                    celAfectate.append((il,ic,iz))
            
            #daca mutarea e valida(daca afecteaza macar 1 celula)
            if celAfectate != []:
                # creez joc nou
                matr_tabla_noua = copy.deepcopy(self.matrCelule)
                jn = Interfata(matr_tabla_noua, Interfata.nrLinii, Interfata.nrColoane,self.capturaPlayer,self.capturaComputer)
                switchPlayer = True
                for (il,ic,iz) in celAfectate:
                    #fac mutarea in jocul nou
                    jn.matrCelule[il][ic].cod|=2**iz
                    # daca mutarea captureaza un patrat
                    if jn.matrCelule[il][ic].cod == 15:
                        # jucatorul isi pastreaza tura
                        switchPlayer = False
                        if jucator == Interfata.JMIN:
                            jn.capturaPlayer.append((il,ic))
                        else:
                            jn.capturaComputer.append((il,ic))
                            
                # adaug tabla noua in lista de mutari posibile
                l_mutari.append((jn,juc_opus if switchPlayer else jucator))
    
        return l_mutari

    def estimeaza_scor(self, adancime,tip_estimat="estimare_1"):
        """Estimeaza scorul pentru tabla curenta.

        Args:
            adancime (int): Adancimea in arborele de decizie
            tip_estimat (str, optional): Ce estimare folosesc pentru scor. Defaults to "estimare_1".

        Returns:
            int: Scorul pe tabla (valori pozitive = mai bine pentru calculator, valori negative = mai bine pentru jucator)
        """
        t_final = self.final()

        # daca starea e finala, in functie de cine a castigat, returneaza un nr ft mare
        if t_final == self.__class__.JMAX:
            return (999 + adancime)
        elif t_final == self.__class__.JMIN:
            return (-999 - adancime)
        elif t_final == 'remiza':
            return 0
        else:
            if tip_estimat == "estimare_1":    
                # Estimarea 1: Nr patratele capturate calculator - nr patratele calculate player = > cu cat nr e mai mare cu atat starea e mai buna pentru MAX   
                return len(self.capturaComputer) -len(self.capturaPlayer)
            else:
                # Estimarea 2: Nr patratele capturate calculator - nr patratele calculate player + nr patratele aproape complete (3/4 ziduri)

                #iau celulele cu 3 pereti selectati
                celule_capturabile = 0
                for lin in self.matrCelule:
                    for cel in lin:
                        # 0bXXXX e codul fiecarei celule, fiecare pozitie ii corespunde unui zid, daca am 3 de 1 => am 3 pereti selectati
                        if cel.cod in [0b1110,0b1101, 0b1011, 0b0111]:
                            celule_capturabile+=1
                # la fel, cu cat nr e mai mare cu atat starea e mai buna pt MAx (pe langa ce am capturat deja, iau in calcul si ce pot sa mai capturez)
                return len(self.capturaComputer) - len(self.capturaPlayer) + celule_capturabile

    def aplica_mutare_player(self,pos):
        """Aplica mutarea jucatorului, daca a dat click pe un zid necapturat deja.

        Args:
            pos ((x,y)): Pozitia cursorului la click

        Returns:
            (bool,bool): (daca a dat click corect, daca a capturat un patratel(pt a mai primi o mutare))
        """
        zidGasit=[]

        for il, linie in enumerate(self.matrCelule):
            for ic, cel in enumerate(linie):                    
                for iz,zid in enumerate(cel.zid):
                    if zid and zid.collidepoint(pos) and not cel.exista_zid(iz):
                        zidGasit.append((il,ic,cel,iz))

        celuleAfectate, aCapturat = self.alege_zid(zidGasit)
        if celuleAfectate is None:
            return False, False

        return True, aCapturat

    
    def alege_zid(self,zidGasit):
        """Marcheaza zidul ca fiind ales.
        

        Args:
            zidGasit ((int,int,Celula,int)): (i_linie,i_coloana,celula afectata, i_zid)

        Returns:
            ([Celula],bool): Ce celule a modificat acest click, daca a fost capturat un patratel in urma mutarii.
        """
        celuleAfectate = []
        aCapturat = False
        if zidGasit == []:
            return None, False

        for (il,ic,cel,iz) in zidGasit:
            cel.cod|=2**iz
            if cel.cod == 15:
                self.capturaPlayer.append((il,ic))
                aCapturat = True
            celuleAfectate.append(cel)

        return celuleAfectate, aCapturat


    @classmethod
    def jucator_opus(cls, jucator):
        """Returneaza jucatorul opus celui dat.
        """
        return cls.JMAX if jucator==cls.JMIN else cls.JMIN



    @classmethod
    def initializeaza(cls,tip_joc,dificultate,nr_linii,nr_coloane,simbol_player):
        """Initializeaza membrii statici ai clasei Interfata cu diferite valori comune tuturor tablelor de joc.

        Args:
            tip_joc (string): minimax/alphabeta
            dificultate (int): 0,1,sau 2
            nr_linii (int): nr linii tabla
            nr_coloane (int): nr coloane tabla
            simbol_player (string): x sau 0
        """

        cls.dimCelula=80
        cls.paddingCelula=5
        cls.dimImagine=cls.dimCelula-2*cls.paddingCelula
        cls.dotSurface = None
        cls.nrLinii = nr_linii
        cls.nrColoane = nr_coloane
        cls.JMIN = simbol_player
        cls.JMAX = '0' if simbol_player == 'X' else 'X'
        cls.scor_maxim = nr_coloane*nr_linii
        
        img_x = pygame.image.load('src/x.png')
        img_0 = pygame.image.load('src/zero.png')
        img_x = pygame.transform.scale(img_x, (cls.dimImagine,cls.dimImagine))
        img_0 = pygame.transform.scale(img_0,  (cls.dimImagine,cls.dimImagine))




        cls.img_player = img_x if simbol_player == 'X' else img_0
        cls.img_computer = img_0 if simbol_player == 'X' else img_x
        Config.set(tip_joc,dificultate,nr_coloane*cls.dimCelula+60,nr_linii*cls.dimCelula+60)
        cls.dotSurface = pygame.surface.Surface((Config.latime_ecran,Config.lungime_ecran),pygame.SRCALPHA, 32)

    def afiseazaDebug(self):
        """Afiseaza matricea de debug.
        """
        print("\nMatrice interfata: ")
        for l in self.matrCelule:
            for  c in l:
                print(c.cod,end=" ")
            print()


            

class Stare:
    """
    Clasa folosita de algoritmii minimax si alpha-beta
    Are ca proprietate tabla de joc
    Functioneaza cu conditia ca in cadrul clasei Joc sa fie definiti JMIN si JMAX (cei doi jucatori posibili)
    De asemenea cere ca in clasa Joc sa fie definita si o metoda numita mutari() care ofera lista cu configuratiile posibile in urma mutarii unui jucator
    """
    def __init__(self, tabla_joc, j_curent, adancime, parinte=None, scor=None):
        self.tabla_joc=tabla_joc
        self.j_curent=j_curent
        
        #adancimea in arborele de stari
        self.adancime=adancime    
        
        #scorul starii (daca e finala) sau al celei mai bune stari-fiice (pentru jucatorul curent)
        self.scor=scor
        
        #lista de mutari posibile din starea curenta
        self.mutari_posibile=[]
        
        #cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        self.stare_aleasa=None



    def update(self,stare_actualizata):
        """Copiaza valorile starii actualizate in self. Folosit pentru a randa tabla de joc fara sa dea flicker.

        Args:
            stare_actualizata (Stare): Starea returnata de algoritmul de alegere a mutarii.
        """
        self.tabla_joc.matrCelule = stare_actualizata.tabla_joc.matrCelule
        self.tabla_joc.capturaComputer = stare_actualizata.tabla_joc.capturaComputer
        self.tabla_joc.capturaPlayer = stare_actualizata.tabla_joc.capturaPlayer
        self.tabla_joc.ultima_mutare = stare_actualizata.tabla_joc.ultima_mutare
        self.j_curent = stare_actualizata.j_curent
        

    def mutari(self):        
        """Expandeaza starea.

        Returns:
            [Stari]: Lista de stari ce pot fi obtinute din starea curenta.
        """
        #iau toate tablele cu mutari noi facute
        l_mutari=self.tabla_joc.mutari(self.j_curent)

        # creez cate o stare pt fiecare mutare noua, si cobor in adancime
        l_stari_mutari=[Stare(mutare, juc, self.adancime-1, parinte=self) for (mutare,juc) in l_mutari]
        return l_stari_mutari

    def __str__(self):
        sir= "Stare("+str(self.tabla_joc.matrCelule) + "(Juc curent:"+self.j_curent+"))\n"
        return sir    
    def __repr__(self):
        sir= "Stare("+str(self.tabla_joc.matrCelule) + "(Juc curent:"+self.j_curent+"))\n"
        return sir
    


def def_val():
    """Folosesc defaultdict la un moment dat asa ca am avut nevoie de functia asta care sa mi returneze o lista goala

    Returns:
        []: Empty list
    """
    return []