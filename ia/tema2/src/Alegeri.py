import pygame
import sys 

class Buton:
    def __init__(self, display=None, left=0, top=0, w=0, h=0,culoareFundal=(89,134,194), culoareFundalSel=(53,80,115), text="", font="arial", fontDimensiune=16, culoareText=(255,255,255), valoare=""):
        self.display=display        
        self.culoareFundal=culoareFundal
        self.culoareFundalSel=culoareFundalSel
        self.text=text
        self.font=font
        self.w=w
        self.h=h
        self.selectat=False
        self.fontDimensiune=fontDimensiune
        self.culoareText=culoareText
        #creez obiectul font
        fontObj = pygame.font.SysFont(self.font, self.fontDimensiune)
        self.textRandat=fontObj.render(self.text, True , self.culoareText) 
        self.dreptunghi=pygame.Rect(left, top, w, h) 
        #aici centram textul
        self.dreptunghiText=self.textRandat.get_rect(center=self.dreptunghi.center)
        self.valoare=valoare

    def selecteaza(self,sel):
        self.selectat=sel
        self.deseneaza()

    def selecteazaDupacoord(self,coord):
        if self.dreptunghi.collidepoint(coord) and self.selectat == False:
            self.selecteaza(True)
            return True
        return False

    def updateDreptunghi(self):
        self.dreptunghi.left=self.left
        self.dreptunghi.top=self.top
        self.dreptunghiText=self.textRandat.get_rect(center=self.dreptunghi.center)

    def deseneaza(self):
        culoareF= self.culoareFundalSel if self.selectat else self.culoareFundal
        pygame.draw.rect(self.display, culoareF, self.dreptunghi)    
        self.display.blit(self.textRandat ,self.dreptunghiText) 

class GrupButoane:
    def __init__(self, listaButoane=[], indiceSelectat=0, spatiuButoane=10,left=0, top=0):
        self.listaButoane=listaButoane
        self.indiceSelectat=indiceSelectat
        self.listaButoane[self.indiceSelectat].selectat=True
        self.top=top
        self.left=left
        leftCurent=self.left
        for b in self.listaButoane:
            b.top=self.top
            b.left=leftCurent
            b.updateDreptunghi()
            leftCurent+=(spatiuButoane+b.w)

    def selecteazaDupacoord(self,coord):
        for ib,b in enumerate(self.listaButoane):
            if b.selecteazaDupacoord(coord):
                self.listaButoane[self.indiceSelectat].selecteaza(False)
                self.indiceSelectat=ib
                return True
        return False

    def deseneaza(self):
        #atentie, nu face wrap
        for b in self.listaButoane:
            b.deseneaza()

    def getValoare(self):
        return self.listaButoane[self.indiceSelectat].valoare


def deseneaza_alegeri(display):
    btn_alg=GrupButoane(
        top=30, 
        left=30,  
        listaButoane=[
            Buton(display=display, w=80, h=30, text="minimax", valoare="minimax"), 
            Buton(display=display, w=90, h=30, text="alphabeta", valoare="alphabeta")
            ],
        indiceSelectat=1)

    btn_est=GrupButoane(
        top=100, 
        left=30, 
        listaButoane=[
            Buton(display=display, w=100, h=30, text="estimare_1", valoare="estimare_1"), 
            Buton(display=display, w=100, h=30, text="estimare_2", valoare="estimare_2")
            ]) 

    btn_juc=GrupButoane(
        top=170, 
        left=30, 
        listaButoane=[
            Buton(display=display, w=35, h=30, text="x", valoare="X"), 
            Buton(display=display, w=45, h=30, text="zero", valoare="0")
            ], 
        indiceSelectat=0)

    btn_dif=GrupButoane(
        top=240, 
        left=30, 
        listaButoane=[
            Buton(display=display, w=60, h=30, text="usor", valoare="0"), 
            Buton(display=display, w=60, h=30, text="mediu", valoare="1"),
            Buton(display=display, w=60, h=30, text="greu", valoare="2"),

            ], 
        indiceSelectat=1)
    ok=Buton(display=display, top=310, left=30, w=40, h=30, text="ok", culoareFundal=(155,0,55))
    btn_alg.deseneaza()
    btn_juc.deseneaza()
    btn_dif.deseneaza()
    btn_est.deseneaza()
    ok.deseneaza()
    while True:
        for ev in pygame.event.get(): 
            if ev.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif ev.type == pygame.MOUSEBUTTONDOWN: 
                pos = pygame.mouse.get_pos()
                if not btn_alg.selecteazaDupacoord(pos):
                    if not btn_juc.selecteazaDupacoord(pos):
                        if not btn_dif.selecteazaDupacoord(pos):
                            if not btn_est.selecteazaDupacoord(pos):
                                if ok.selecteazaDupacoord(pos):
                                    # display.fill((0,0,0)) #stergere ecran 
                                    # tabla_curenta.deseneaza_grid()
                                    return btn_alg.getValoare(), btn_dif.getValoare(), btn_juc.getValoare(),btn_est.getValoare()
        pygame.display.update()