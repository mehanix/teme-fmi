import pygame

class Config:

    @classmethod
    def set(cls,tip_joc,dificultate, lat, lung):
        cls.tip_joc = tip_joc
        cls.dificultate = dificultate
        cls.latime_ecran = lat
        cls.lungime_ecran = lung
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

    def __init__ (self, left, top, w, h, display, lin, col,interfata, cod=0):
        self.dreptunghi=pygame.Rect(left, top, w, h)
        self.display=display
        self.zid=[None,None,None,None]
        #zidurile vor fi pe pozitiile 0-sus, 1-dreapta, 2-jos, 3-stanga
        self.cod=0
        self.zid[0]=pygame.Rect(left,top-1-self.__class__.grosimeZid//2, w,self.__class__.grosimeZid)

        self.zid[1]=pygame.Rect(left+w-self.__class__.grosimeZid//2,top, self.__class__.grosimeZid, h)

        self.zid[2]=pygame.Rect(left,top+h-self.__class__.grosimeZid//2, w,self.__class__.grosimeZid)

        self.zid[3]=pygame.Rect(left-1-self.__class__.grosimeZid//2,top, self.__class__.grosimeZid,h)
   

        #print(self.zid)
        #0001 zid doar sus
        #0011 zid sus si dreapta etc
    def deseneaza(self):
        pygame.draw.rect(self.display, self.__class__.fundalCelula, self.dreptunghi)
        #masti=[1,2,4,8]
        masca=1
        for i in range(4):
            if self.cod & masca:
                if self.zid[i]:
                    pygame.draw.rect(self.display, self.__class__.culoareLinii, self.zid[i])        
            masca*=2

                # top left
        
        pygame.draw.circle(Interfata.dotSurface,self.culoarePuncte,(self.dreptunghi.x,self.dreptunghi.y),self.razaPuncte)
        #top right
        pygame.draw.circle(Interfata.dotSurface,self.culoarePuncte,(self.dreptunghi.x,self.dreptunghi.y + self.dreptunghi.w),self.razaPuncte)
        pygame.draw.circle(Interfata.dotSurface,self.culoarePuncte,(self.dreptunghi.x+self.dreptunghi.h,self.dreptunghi.y + self.dreptunghi.w),self.razaPuncte)
        pygame.draw.circle(Interfata.dotSurface,self.culoarePuncte,(self.dreptunghi.x+self.dreptunghi.h,self.dreptunghi.y),self.razaPuncte)



class Interfata:
    culoareEcran=(255,255,255)
    JMIN = None #player
    JMAX = None #computer

    def __init__(self, nrLinii=7, nrColoane=10):
        self.ultima_mutare = None

        self.nrLinii=nrLinii
        self.nrColoane=nrColoane
        self.matrCelule=[[Celula(display=Config.ecran, left=col*(self.__class__.dimCelula+1)+30, top=lin*(self.__class__.dimCelula+1)+30, w=self.__class__.dimCelula, h=self.__class__.dimCelula, lin=lin, col=col, interfata=self) for col in range(nrColoane)] for lin in range(nrLinii) ]
 
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

    @classmethod
    def initializeaza(cls,tip_joc,dificultate,nr_linii,nr_coloane):

        cls.dimCelula=80
        cls.paddingCelula=5
        cls.dimImagine=cls.dimCelula-2*cls.paddingCelula
        cls.dotSurface = None
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