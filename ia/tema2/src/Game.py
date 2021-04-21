import pygame
import copy

class Config:

    @classmethod
    def set(cls,tip_joc,dificultate, lat, lung):
        cls.tip_joc = tip_joc
        cls.dificultate = dificultate
        cls.latime_ecran = lat
        cls.lungime_ecran = lung
        cls.ADANCIME_MAX = 3
 
    @classmethod
    def set_ecran(cls,ecr):
        cls.ecran = ecr
class Celula:
    #coordonatele nodurilor ()
    grosimeZid=11 #numar impar
    fundalCelula=(255,255,255)
    culoareLinii=(0,0,0)
    culoarePuncte = (0,0,0)
    razaPuncte = 12
    afisImagini=True

    def __init__ (self, left, top, w, h,  lin, col,interfata, cod=0):
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
        pygame.draw.rect(Config.ecran, self.__class__.fundalCelula, self.dreptunghi)
        #masti=[1,2,4,8]
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
        print(self.cod & 2**i_zid)
        return self.cod & 2**i_zid

    def __repr__(self):
        return "Celula " + str(self.dreptunghi.x) + '  ' + str(self.dreptunghi.y)

class Interfata:
    culoareEcran=(255,255,255)
    JMIN = None #player
    JMAX = None #computer

    def __init__(self, matr, nrLinii=7, nrColoane=10):
        self.ultima_mutare = None
        self.nrLinii=nrLinii
        self.nrColoane=nrColoane
        self.matrCelule=matr if matr is not None else [[Celula(left=col*(self.__class__.dimCelula+1)+30, top=lin*(self.__class__.dimCelula+1)+30, w=self.__class__.dimCelula, h=self.__class__.dimCelula, lin=lin, col=col, interfata=self) for col in range(nrColoane)] for lin in range(nrLinii) ]
        
        self.matCoordZiduri = self.getMatCoordZiduri(self.matrCelule)


    def getMatCoordZiduri(self,matr):
        coords = set()
        print(matr)
        for lin in matr:
            for cel in lin:
                for zid in cel.zid:
                    coords.add(zid.center)
        print(coords)
        return coords

    def deseneazaImag(self, imag, cel):
        Config.ecran.blit(imag,(cel.dreptunghi.left+self.__class__.paddingCelula,  cel.dreptunghi.top+self.__class__.paddingCelula))

    def deseneazaEcranJoc(self):
        Config.ecran.fill(self.__class__.culoareEcran)
        for linie in self.matrCelule:
            for cel in linie:
                cel.deseneaza()  
                print(cel.cod)
                if cel.cod == 15:
                    self.deseneazaImag(self.img_x, cel)
        pygame.display.update()

    #mutari calculator, yay
    def mutari(self,jucator):
        l_mutari = []

        #iterez prin toata tabla mea
        # pt fiecare zid, iau celulele pe care selectarea lui le va afecta
        for pos in self.matCoordZiduri:
            zidGasit = []
            for il, linie in enumerate(self.matrCelule):
                for ic, cel in enumerate(linie):                    
                    for iz,zid in enumerate(cel.zid):
                        if zid and zid.collidepoint(pos) and not cel.exista_zid(iz):
                                zidGasit.append((il,ic,iz))
        
            if zidGasit != []:
                matr_tabla_noua = copy.deepcopy(self.matrCelule)
                for (il,ic,iz) in zidGasit:
                    matr_tabla_noua[il][ic].cod|=2**iz
                jn = Interfata(matr_tabla_noua, Interfata.nrLinii, Interfata.nrColoane)

                l_mutari.append(jn)
        return l_mutari

    def aplica_mutare_player(self,pos):
        zidGasit=[]

        for il, linie in enumerate(self.matrCelule):
            for ic, cel in enumerate(linie):                    
                for iz,zid in enumerate(cel.zid):
                    if zid and zid.collidepoint(pos) and not cel.exista_zid(iz):
                        zidGasit.append((cel,iz,zid))

        celuleAfectate = self.alege_zid(zidGasit)
        if celuleAfectate is None:
            return False  
        #self.update_valori(celuleAfectate)
        return True

    def aplica_mutare_computer(self):
        return NotImplemented
    
    def alege_zid(self,zidGasit):
        celuleAfectate = []
        if zidGasit == []:
            return

        for (cel,iz,zid) in zidGasit:
            #pygame.draw.rect(Config.ecran, Celula.culoareLinii,zid)
            cel.cod|=2**iz
            celuleAfectate.append(cel)
        return celuleAfectate

    #def update_valori(self,celuleAfectate):
        #for celA in celuleAfectate:
            #if celA.cod==15:
                #self.deseneazaImag(Interfata.img_x, celA)



    @classmethod
    def jucator_opus(cls, jucator):
        return cls.JMAX if jucator==cls.JMIN else cls.JMIN


    @classmethod
    def initializeaza(cls,tip_joc,dificultate,nr_linii,nr_coloane):

        cls.dimCelula=80
        cls.paddingCelula=5
        cls.dimImagine=cls.dimCelula-2*cls.paddingCelula
        cls.dotSurface = None
        cls.nrLinii = nr_linii
        cls.nrColoane = nr_coloane
        cls.img_x = pygame.image.load('src/x.png')
        cls.img_0 = pygame.image.load('src/zero.png')
        cls.img_x = pygame.transform.scale(cls.img_x, (cls.dimImagine,cls.dimImagine))
        cls.img_0 = pygame.transform.scale(cls.img_0,  (cls.dimImagine,cls.dimImagine))
        Config.set(tip_joc,dificultate,nr_coloane*cls.dimCelula+60,nr_linii*cls.dimCelula+60)
        cls.dotSurface = pygame.surface.Surface((Config.latime_ecran,Config.lungime_ecran),pygame.SRCALPHA, 32)

    def afiseazaDebug(self):
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



    def mutari(self):        
        l_mutari=self.tabla_joc.mutari(self.j_curent)
        juc_opus=Interfata.jucator_opus(self.j_curent)

        l_stari_mutari=[Stare(mutare, juc_opus, self.adancime-1, parinte=self) for mutare in l_mutari]
        return l_stari_mutari
        
    
    def __str__(self):
        sir= "Stare("+str(self.tabla_joc.matrCelule) + "(Juc curent:"+self.j_curent+"))\n"
        return sir    
    def __repr__(self):
        sir= "Stare("+str(self.tabla_joc.matrCelule) + "(Juc curent:"+self.j_curent+"))\n"
        return sir
    