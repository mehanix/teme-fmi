import copy
import time
from src.graph import *

def a_star(start,scopuri,out):
	out.write("#######################################\n")
	out.write("#                  A*                 #\n")
	out.write("#######################################\n")

	gr = Graph(start, scopuri)
	astar(gr,out)

def astar(gr, out):
	print("astar")

	c = [ NodParcurgere(gr.start, 0, None) ]
	while len(c) > 0:

		current_time = time.time()
		if (round(gr.start_time - current_time) > gr.timeout):
			out.write("Timeout!")
			return


		nodCurent = c.pop(0)
		print(nodCurent.info, nodCurent.g,nodCurent.h,nodCurent.f)
		# daca e solutie, afisam si scadem nr de solutii
		if gr.testeaza_scop(nodCurent):
			nodCurent.afisDrum(len(c))
			out.write("\n----------------\n")
			gr.nsol -= 1
			
			if gr.nsol==0:
				return

		# generez succesori
		lSuccesori=gr.genereazaSuccesori(nodCurent)	

		for s in lSuccesori:
			i=0
			gasit_loc=False
			for i in range(len(c)):
				#diferenta fata de UCS e ca ordonez dupa f
				if c[i].f>=s.f :
					gasit_loc=True
					break
			if gasit_loc:
				c.insert(i,s)
			else:
				c.append(s)
