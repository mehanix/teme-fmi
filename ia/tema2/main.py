import pygame
import sys
import src.Game as game
import random
import time
pygame.init()

# TODO: interfata selectare aici
tip_joc = "minimax"
dificultate = "1"
nr_linii = 3
nr_coloane = 3
game.Interfata.initializeaza(tip_joc,dificultate,nr_linii,nr_coloane)
game.Interfata.JMIN = 'X'
game.Interfata.JMAX = '0'


ecr = pygame.display.set_mode(size=(game.Config.latime_ecran,game.Config.lungime_ecran))
game.Config.set_ecran(ecr)
tabla_curenta = game.Interfata(None,nr_linii,nr_coloane)
tabla_curenta.deseneazaEcranJoc()
tabla_curenta.afiseazaDebug()

stare_curenta = game.Stare(tabla_curenta,'X',game.Config.ADANCIME_MAX)
while True:
######### USER
    if (stare_curenta.j_curent == game.Interfata.JMIN):
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif ev.type == pygame.MOUSEBUTTONDOWN: 
                pos = pygame.mouse.get_pos()
                mutare_corecta = stare_curenta.tabla_joc.aplica_mutare_player(pos)
                if mutare_corecta:
                    # tabla_curenta.afiseazaDebug()
                    stare_curenta.j_curent = game.Interfata.jucator_opus(stare_curenta.j_curent)
                    tabla_curenta.deseneazaEcranJoc()            
            ecr.blit(game.Interfata.dotSurface,(0,0))

 ######### COMPUTER
    else:
        print("pc turn")
        # TODO: ai stuff
        stari_noi = stare_curenta.mutari()

        # TODO: aici bagi minmax
        stare_actualizata = stari_noi[random.randrange(len(stari_noi))]
        stare_curenta.tabla_joc = stare_actualizata.tabla_joc
        time.sleep(0.2)
        stare_curenta.tabla_joc.deseneazaEcranJoc()
        stare_curenta.j_curent = game.Interfata.jucator_opus(stare_curenta.j_curent)




    pygame.display.update()