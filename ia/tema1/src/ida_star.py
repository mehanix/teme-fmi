import copy
import time
from src.graph import *

max_ida = 0
def construieste_drum(nodCurent: NodParcurgere, limita, out, gr,nmax=0):
    global max_ida
    max_ida = max(max_ida,nmax)
    if nodCurent.info == gr.scopuri:
        nodCurent.afisDrum(max_ida)
        return (True, 0)
    
    if nodCurent.f > limita:
        return(False, nodCurent.f)
    
    mini = float('inf')

    current_time = time.time()
    if (round(current_time - gr.start_time) > gr.timeout):
        out.write("Timeout!\n")
        return (True, mini)

    succesori = gr.genereazaSuccesori(nodCurent)
    for nod in succesori:
        (ajuns, lim) = construieste_drum(nod, limita, out, gr, nmax+len(succesori))
        # info = nod.info
        # g = nod.g
        # h = nod.h 
        # key = nod.key
        # (ajuns, lim) = construieste_drum(NodParcurgere(info, g, nodCurent, key, h), limita,out, gr, nmax+len(succesori))
        if ajuns:
            return(True, 0)
        mini = min(mini, lim)

    return (False, mini)






def ida_star(start,scopuri,out,euristica="banala"):
    """Wrapper pentru algoritmul IDA*. Pregateste graful problemei si ruleaza algoritmul.

    Args:
        start ([Incuietoare]): Configuratia de start (toate incuietorile pe 1)
        scopuri ([Incuietoare]): Configuratia de stop (toate incuietorile pe 0)
        out (IO): Fisierul de iesire
        euristica(string): ce euristica voi folosi in estimarea costului drumului nodCurent -> stareScop
    """
    out.write("########################################\n")
    out.write("#                 IDA*                 #\n")
    out.write("########################################\n")
    msg = "Euristica: " + euristica
    spaces = (38 - len(msg))//2
    out.write("#" + " "*spaces + msg + " "*(spaces+1) + "#\n")
    out.write("########################################\n")

    NodParcurgere.out = out
    global max_ida
    max_ida = 0
    gr = Graph(start, scopuri,euristica)
    _idastar(gr,out)

def _idastar(gr, out):
    """Ruleaza IDA* pe graful gr si scrie rezultatele in out.

    Args:
        gr (graph): Graful problemei
        out (IO): Fisier iesire.
    """
    print("idastar")

    #niv = h(startNod) facem dfs din nodurile care au niv >= f, daca f > niv nu apelam dfs pe succesori, 
    #niv = min({f(nod) | f(nod) > niv si nod este o frunza a arborelui expandat})
    nivel = gr.calculeaza_h(gr.start)
    nodStart = NodParcurgere(gr.start, 0,None, None, gr.calculeaza_h(gr.start))
    while True:
        (ajuns, lim) = construieste_drum(nodStart, nivel,out,gr)
        if ajuns:
            break
        if lim == float('inf'):
            break
        nivel = lim