import src.Game as game

nrNoduriGen = 0
def alpha_beta(alpha, beta, stare):
    global nrNoduriGen
    nrNoduriGen+=1
    if stare.adancime==0 or stare.tabla_joc.final() :
        stare.scor=stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare
    
    if alpha>beta:
        return stare #este intr-un interval invalid deci nu o mai procesez
    
    stare.mutari_posibile=stare.mutari()


    if stare.j_curent==game.Interfata.JMAX :
        scor_curent=float('-inf')
        
        for mutare in stare.mutari_posibile:
            #calculeaza scorul
            stare_noua=alpha_beta(alpha, beta, mutare)
            
            if (scor_curent<stare_noua.scor):
                stare.stare_aleasa=stare_noua
                scor_curent=stare_noua.scor
            if(alpha<stare_noua.scor):
                alpha=stare_noua.scor
                if alpha>=beta:
                    break

    elif stare.j_curent==game.Interfata.JMIN :
        scor_curent=float('inf')
        
        for mutare in stare.mutari_posibile:
            
            stare_noua=alpha_beta(alpha, beta, mutare)
            
            if (scor_curent>stare_noua.scor):
                stare.stare_aleasa=stare_noua
                scor_curent=stare_noua.scor

            if(beta>stare_noua.scor):
                beta=stare_noua.scor
                if alpha>=beta:
                    break
    stare.scor=stare.stare_aleasa.scor

    return stare
    


