import src.Game as game

nrNoduriGen = 0
def min_max(stare,tip_estimat):
    global nrNoduriGen
    nrNoduriGen +=1
    if stare.adancime==0 or stare.tabla_joc.final() :
        stare.scor=stare.tabla_joc.estimeaza_scor(stare.adancime,tip_estimat)
        return stare
        
    #calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile=stare.mutari()

    #aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutari_scor=[min_max(mutare) for mutare in stare.mutari_posibile]
    


    if stare.j_curent==game.Interfata.JMAX :
        #daca jucatorul e JMAX aleg starea-fiica cu scorul maxim
        stare.stare_aleasa=max(mutari_scor, key=lambda x: x.scor)
    else:
        #daca jucatorul e JMIN aleg starea-fiica cu scorul minim
        stare.stare_aleasa=min(mutari_scor, key=lambda x: x.scor)
    stare.scor=stare.stare_aleasa.scor
    return stare