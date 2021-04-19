import copy
import time
from src.graph import *

def a_star_v2(start,scopuri,out,euristica="banala"):
    out.write("########################################\n")
    out.write("#   A* - open/closed, doar sol min     #\n")
    out.write("########################################\n")
    msg = "Euristica: " + euristica
    spaces = (38 - len(msg))//2
    out.write("#" + " "*spaces + msg + " "*(spaces+1) + "#\n")
    out.write("########################################\n")

    gr = Graph(start, scopuri,euristica)
    astar_v2(gr,out)


def in_list(nod_info, lista):
  for nod in lista:
    if nod_info == nod.info:
      return nod
  return None

def insert(node, lista):
  idx = 0
  while idx < len(lista) - 1 and (node.f > lista[idx].f or (node.f == lista[idx].f and node.g < lista[idx].g)):
    idx += 1
  lista.insert(idx, node)

def astar_v2(gr, out):
    print("astar_v2")
    #de completat
    opened = [NodParcurgere(gr.start, 0, None)]

    closed = []

    continua = True

    while continua and len(opened) > 0:
        Graph.maxim = max(Graph.maxim, len(opened) + len(closed))
        current_time = time.time()
        if (round(current_time - gr.start_time) > gr.timeout):
            out.write("Timeout!\n")
            return

        current_node = opened.pop(0)
        closed.append(current_node)

        if current_node.info == gr.scopuri:
            current_node.afisDrum(len(opened))
            continua = False

        succesori = gr.genereazaSuccesori(current_node)
        for nod in succesori:
            info = nod.info
            g = nod.g
            h = nod.h
            key = nod.key
            node_open = in_list(info, opened)
            node_parc = NodParcurgere(info, g, current_node,key, h)
            if node_open is not None:
                if node_open.f > g + h:
                    opened.remove(node_open)
                    insert(node_parc, opened)
                continue
            node_closed = in_list(info, closed)
            if node_closed is not None:
                if node_closed.f > g + h:
                    closed.remove(node_closed)
                    insert(node_parc, opened)
                continue
            insert(node_parc, opened)
    
    if len(opened) == 0:
        print("Nu exista drum!")
    


    # c = [ NodParcurgere(gr.start, 0, None) ]
    # while len(c) > 0:
    #     Graph.maxim = max(Graph.maxim, len(c))
    #     current_time = time.time()
    #     if (round(current_time - gr.start_time) > gr.timeout):
    #         out.write("Timeout!\n")
    #         return


    #     nodCurent = c.pop(0)
    #     # print(nodCurent.info, nodCurent.g,nodCurent.h,nodCurent.f)
    #     # daca e solutie, afisam si scadem nr de solutii
    #     if gr.testeaza_scop(nodCurent):
    #         nodCurent.afisDrum(len(c))
    #         out.write("\n----------------\n")
    #         gr.nsol -= 1
            
    #         if gr.nsol==0:
    #             return

    #     # generez succesori
    #     lSuccesori=gr.genereazaSuccesori(nodCurent)    

    #     for s in lSuccesori:
    #         i=0
    #         gasit_loc=False
    #         for i in range(len(c)):
    #             #diferenta fata de UCS e ca ordonez dupa f
    #             if c[i].f>=s.f :
    #                 gasit_loc=True
    #                 break
    #         if gasit_loc:
    #             c.insert(i,s)
    #         else:
    #             c.append(s)
