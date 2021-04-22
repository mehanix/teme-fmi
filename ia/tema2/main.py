import pygame
import sys
import src.Game as game
import random
import time
import copy
import src.Alegeri as alegeri
import src.Minmax as m

def afis_daca_final(stare_curenta):

    final=stare_curenta.tabla_joc.final()
    if(final):
        if (final=="remiza"):
            print("Remiza!")
        else:
            print("A castigat "+final)
            
        return True
        
    return False

def main():
    pygame.init()
    pygame.display.set_caption("Dots and Boxes - Nicoleta Ciausu")

    ##### SETUP
    ecr = pygame.display.set_mode(size=(300,300))
    tip_joc, dificultate, simbol_player = alegeri.deseneaza_alegeri(ecr)
    print(tip_joc,dificultate,simbol_player)

    nr_linii = 3
    nr_coloane = 3

    game.Interfata.initializeaza(tip_joc,dificultate,nr_linii,nr_coloane,simbol_player)


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
                        if(stare_curenta.tabla_joc.final()):
                            break 
            ecr.blit(game.Interfata.dotSurface,(0,0))

    ######### COMPUTER
        else:
            print("pc turn")
            # TODO: ai stuff
            stari_noi = stare_curenta.mutari()

            # TODO: aici bagi minmax
            if len(stari_noi):
                stare_actualizata = m.min_max(stare_curenta)
                # stare_actualizata = stari_noi[random.randrange(len(stari_noi))]
                # TODO: if stuff acts weird, investigate
                stare_curenta.update(stare_actualizata.stare_aleasa)
                # stare_curenta.tabla_joc.matrCelule = stare_actualizata.tabla_joc.matrCelule
                stare_curenta.tabla_joc.deseneazaEcranJoc()

                end = afis_daca_final(stare_curenta)
                if(end):
                    pygame.display.update()
                    return end 
                stare_curenta.j_curent = game.Interfata.jucator_opus(stare_curenta.j_curent)
            else:
                stare_curenta.tabla_joc.deseneazaEcranJoc()
                end = afis_daca_final(stare_curenta)
                if(end):
                    pygame.display.update()
                    return end 



        pygame.display.update()

    
if __name__ == "__main__" :
    mesaj = main()

    print(mesaj)
    while True :
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()