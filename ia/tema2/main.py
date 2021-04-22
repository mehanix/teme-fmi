import pygame
import sys
import src.Game as game
import random
import time
import copy
import src.Alegeri as alegeri

def main():
    pygame.init()
    pygame.display.set_caption("Dots and Boxes - Nicoleta Ciausu")

    ##### SETUP
    ecr = pygame.display.set_mode(size=(300,300))
    tip_joc, dificultate, simbol_player = alegeri.deseneaza_alegeri(ecr)
    print(tip_joc,dificultate,simbol_player)

    nr_linii = 3
    nr_coloane = 3

    game.Interfata.initializeaza(tip_joc,dificultate,nr_linii,nr_coloane)
    game.Interfata.JMIN = simbol_player
    game.Interfata.JMAX = '0' if simbol_player == 'X' else 'X'

    ##### Incep joc
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
                        if(stare_curenta.tabla_joc.eStareFinala()):
                            break 
            ecr.blit(game.Interfata.dotSurface,(0,0))

    ######### COMPUTER
        else:
            print("pc turn")
            # TODO: ai stuff
            stari_noi = stare_curenta.mutari()

            # TODO: aici bagi minmax
            if len(stari_noi):
                stare_actualizata = stari_noi[random.randrange(len(stari_noi))]
                # TODO: if stuff acts weird, investigate
                stare_curenta.tabla_joc.matrCelule = stare_actualizata.tabla_joc.matrCelule
                time.sleep(0.2)
                stare_curenta.tabla_joc.deseneazaEcranJoc()

                if(stare_curenta.tabla_joc.eStareFinala()):
                    break
                stare_curenta.j_curent = game.Interfata.jucator_opus(stare_curenta.j_curent)
            else:
                stare_curenta.tabla_joc.deseneazaEcranJoc()
                if(stare_curenta.tabla_joc.eStareFinala()):
                    break



        pygame.display.update()

    
if __name__ == "__main__" :
    main()
    while True :
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()