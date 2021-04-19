import copy
import time
from src.graph import *


def construieste_drum(nodCurent: NodParcurgere, limita, gr):
    if nodCurent.info == gr.scopuri:
        nodCurent.afisDrum(-1)
        return (True, 0)
    
    if nodCurent.f > limita:
        return(False, nodCurent.f)
    
    mini = float('inf')

    for nod in gr.genereazaSuccesori(nodCurent):
        info = nod.info
        g = nod.g
        h = nod.h 
        key = nod.key
        (ajuns, lim) = construieste_drum(NodParcurgere(info, g, nodCurent, key, h), limita, gr)
        if ajuns:
            return(True, 0)
        mini = min(mini, lim)

    return (False, mini)


def ida_star(start,scopuri,out,euristica="banala"):
    out.write("########################################\n")
    out.write("#                 IDA*                 #\n")
    out.write("########################################\n")
    msg = "Euristica: " + euristica
    spaces = (38 - len(msg))//2
    out.write("#" + " "*spaces + msg + " "*(spaces+1) + "#\n")
    out.write("########################################\n")

    gr = Graph(start, scopuri,euristica)
    idastar(gr,out)

def idastar(gr, out):
    print("idastar")
    #niv = h(startNod) facem dfs din nodurile care au niv >= f, daca f > niv nu apelam dfs pe succesori, 
    #niv = min({f(nod) | f(nod) > niv si nod este o frunza a arborelui expandat})
    nivel = gr.calculeaza_h(gr.start)
    nodStart = NodParcurgere(gr.start, 0,None, None, gr.calculeaza_h(gr.start))
    while True:
        Graph.maxim = max(Graph.maxim, 0)
        current_time = time.time()
        if (round(current_time - gr.start_time) > gr.timeout):
            out.write("Timeout!\n")
            return

        (ajuns, lim) = construieste_drum(nodStart, nivel,gr)
        if ajuns:
            break
        if lim == float('inf'):
            print("Nu exista drum!")
            break
        nivel = lim