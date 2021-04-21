import pygame
import sys
import src.Game as game
pygame.init()

# TODO: interfata selectare aici
tip_joc = "minimax"
dificultate = "1"
nr_linii = 4
nr_coloane = 4
game.Interfata.initializeaza(tip_joc,dificultate,nr_linii,nr_coloane)
game.Interfata.JMIN = 'X'
game.Interfata.JMAX = '0'


ecr = pygame.display.set_mode(size=(game.Config.latime_ecran,game.Config.lungime_ecran))
game.Config.set_ecran(ecr)
tabla_curenta = game.Interfata(nr_linii,nr_coloane)
tabla_curenta.deseneazaEcranJoc()

tabla_curenta.afiseazaDebug()
while True:        
    for ev in pygame.event.get(): 
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif ev.type == pygame.MOUSEBUTTONDOWN: 
            pos = pygame.mouse.get_pos()
            zidGasit=[]
            for il, linie in enumerate(tabla_curenta.matrCelule):
                for ic, cel in enumerate(linie):                    
                    for iz,zid in enumerate(cel.zid):
                        if zid and zid.collidepoint(pos):
                            zidGasit.append((cel,iz,zid))
            celuleAfectate=[]
            if 0<len(zidGasit)<=2:
                for (cel,iz,zid) in zidGasit:
                    pygame.draw.rect(game.Config.ecran, game.Celula.culoareLinii,zid)
                    cel.cod|=2**iz
                    celuleAfectate.append(cel)   

                #doar de debug
                tabla_curenta.afiseazaDebug()

            for celA in celuleAfectate:
                if celA.cod==15:
                    tabla_curenta.deseneazaImag(game.Interfata.img_x, celA)
        ecr.blit(game.Interfata.dotSurface,(0,0))



    pygame.display.update()