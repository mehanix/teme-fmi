import pygame
import sys
import src.Game as game
import random
import time
import copy
import src.Alegeri as alegeri
import src.Minmax as m
import src.Alphabeta as a
import src.Statistici as s
import math
def afis_daca_final(stare_curenta):
    """Afiseaza raspunsul de final joc, daca starea curenta e stare finala.

    Args:
        stare_curenta (Stare): [Starea curenta a jocului

    Returns:
        string: Mesajul de final de joc, daca jocul e terminat
        False: Daca jocul nu e terminat
    """

    final=stare_curenta.tabla_joc.final()
    if(final):
        if (final=="remiza"):
            return "Remiza!"
        else:
            stare_curenta.tabla_joc.marcheaza(final)
            stare_curenta.tabla_joc.deseneazaEcranJoc()
            return "A castigat "+final
                    
    return False

def main():
    """Functia principala a jocului. Aici are loc atat setup-ul initial, cat si game loop-ul.

    Returns:
        string: Mesajul de final al jocului (cine a castigat)
    """
    pygame.init()
    pygame.display.set_caption("Dots and Boxes - Nicoleta Ciausu")

    ##### SETUP
    ecr = pygame.display.set_mode(size=(300,370))
    
    # ecran selectat alegeri
    tip_joc, dificultate, simbol_player,tip_estimat = alegeri.deseneaza_alegeri(ecr)
    print(tip_joc,dificultate,simbol_player)

    nr_linii = 3
    nr_coloane = 3

    game.Interfata.initializeaza(tip_joc,dificultate,nr_linii,nr_coloane,simbol_player)


    ##### Incep joc
    ecr = pygame.display.set_mode(size=(game.Config.latime_ecran,game.Config.lungime_ecran))
    game.Config.set_ecran(ecr)

    # initializeaza tabla
    tabla_curenta = game.Interfata(None,nr_linii,nr_coloane)
    game.Interfata.getMatCoordZiduri(tabla_curenta.matrCelule)
    tabla_curenta.deseneazaEcranJoc()
    tabla_curenta.afiseazaDebug()

    # starea initiala
    stare_curenta = game.Stare(tabla_curenta,'X',game.Config.ADANCIME_MAX)

    # text pentru randul cui e
    font = pygame.font.SysFont('arial',16)
    text_player = font.render("Randul lui " + game.Interfata.JMIN,True,(0,0,0)).convert_alpha()
    text_pc = font.render("Randul lui " + game.Interfata.JMAX,True,(0,0,0)).convert_alpha()

    text_player_rect = text_player.get_rect()
    text_player_rect.center = (ecr.get_width()//2,ecr.get_height()-25)
    
    #valori statistice
    s.Statistici.timpStartJoc = time.time()
    timpStartUser = None
    timpStartPc = 0
    while True:
    ######### USER
        if (stare_curenta.j_curent == game.Interfata.JMIN):
            if timpStartUser is None:
                timpStartUser = time.time()
            for ev in pygame.event.get(): 
                if ev.type == pygame.QUIT:
                    s.Statistici.showFinalStats()
                    pygame.quit()
                    sys.exit()
                elif ev.type == pygame.MOUSEBUTTONDOWN: 
                    # ia pozitia mouse-ului, daca a dat un click corect efectueaza mutarea
                    pos = pygame.mouse.get_pos()
                    mutare_corecta, a_capturat = stare_curenta.tabla_joc.aplica_mutare_player(pos)
                    if mutare_corecta:
                        timpEndUser = time.time()
                        s.Statistici.nrMutariJMIN+=1
                        timp = round((timpEndUser-timpStartUser)*1000)
                        timpStartUser = None
                        s.Statistici.timpiGandireUser.append(timp)
                        print("Utilizatorul s-a gandit {0}ms".format(timp))
                        tabla_curenta.afiseazaDebug()
                        # daca mutarea a capturat un patratel, ai voie sa mai muti o data
                        if not a_capturat:
                            stare_curenta.j_curent = game.Interfata.jucator_opus(stare_curenta.j_curent)
                        tabla_curenta.deseneazaEcranJoc()

                        # verifica daca stare == stare_finala
                        end = afis_daca_final(stare_curenta)
                        if(end):
                            return end 
            ecr.blit(game.Interfata.dotSurface,(0,0))
            ecr.blit(text_player,text_player_rect)
            pygame.display.update()
    ######### COMPUTER
        else:

            for ev in pygame.event.get(): 
                # la exit prematur, afiseaza statistici pana in punctul jucat
                if ev.type == pygame.QUIT:
                    s.Statistici.showFinalStats()
                    pygame.quit()
                    sys.exit()

            # deseneaza tabla
            stare_curenta.tabla_joc.deseneazaEcranJoc()
            ecr.blit(game.Interfata.dotSurface,(0,0))
            ecr.blit(text_pc,text_player_rect)
            pygame.display.update()

            #initializari pt statistici
            timpStartPc = time.time()
            m.nrNoduriGen = 0
            a.nrNoduriGen = 0
            
            # obtine starea optima in fct de algoritmul selectat
            stare_actualizata = None 

            if tip_joc == "minimax":
                stare_actualizata = m.min_max(stare_curenta,tip_estimat)
            else:
                stare_actualizata = a.alpha_beta(-9999,9999,stare_curenta,tip_estimat)
            
            # calculeaza si afiseaza statistici
            timpEndPc = time.time()
            timp = round((timpEndPc-timpStartPc)*1000)
            s.Statistici.timpiGandirePc.append(timp)
            s.Statistici.nrMutariJMAX+=1
            s.Statistici.nrNoduriGenerate.append(m.nrNoduriGen if tip_joc == "minimax" else a.nrNoduriGen)
            print("Scor user:", str(len(stare_actualizata.tabla_joc.capturaPlayer)))
            print("Scor calculator:", str(len(stare_actualizata.tabla_joc.capturaComputer)))
            print("Calculatorul s-a \"gandit\" {0}ms".format( timp ) )
            estimat = m.nrNoduriGen if tip_joc == "minimax" else a.nrNoduriGen 
            print(f"{tip_joc} a ales starea cu scorul estimat: {stare_actualizata.scor} si pt asta a generat {estimat} noduri")

            # fa noua mutare pe tabla
            stare_curenta.update(stare_actualizata.stare_aleasa)
            #redraw, verifica daca a fost mutare finala
            stare_curenta.tabla_joc.deseneazaEcranJoc()

            end = afis_daca_final(stare_curenta)
            if(end):
                pygame.display.update()
                return end 

    
if __name__ == "__main__" :
    # joaca
    mesaj = main()
    # afiseaza cine a castigat si statisticile
    s.Statistici.showFinalStats()
    font = pygame.font.SysFont('arial',16)
    text_win = font.render(mesaj,True,(0,0,0)).convert_alpha()

    text_win_rect = text_win.get_rect()
    text_win_rect.center = (game.Config.ecran.get_width()//2,game.Config.ecran.get_height()-25)

    game.Config.ecran.blit(text_win,text_win_rect)
    while True :
        game.Config.ecran.blit(game.Interfata.dotSurface,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()