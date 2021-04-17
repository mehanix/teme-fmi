import copy
import time
from src.graph import *

def ucs(start, scopuri,out):
	out.write("#######################################\n")
	out.write("#         Uniform Cost Search         #\n")
	out.write("#######################################\n")

	gr = Graph(start, scopuri)
	uniform_cost(gr,out)


#### algoritm Uniform Cost Search
#presupunem ca vrem mai multe solutii (un numar fix)
#daca vrem doar o solutie, renuntam la variabila nrSolutiiCautate
#si doar oprim algoritmul la afisarea primei solutii


def uniform_cost(gr,out):
	# Initializez cu configuratia de start (toate incuietorile pe 1)
	c = [ NodParcurgere(gr.start, 0, None) ]
	
	while len(c)>0:

		current_time = time.time()
		print(gr.start_time,current_time,gr.timeout, round(gr.start_time - current_time) < gr.timeout)
		if (round(gr.start_time - current_time) > gr.timeout):
			out.write("Timeout!")
			return
		# print(c)

		# input()
		
		# iau element curent
		nodCurent=c.pop(0)
		
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
			i = 0
			gasit_loc = False

			# tin coada a.i. sa fie ordonata crescator dupa cost
			for i in range(len(c)):
				#ordonez dupa cost(notat cu g aici și în desenele de pe site)
				if c[i].g>s.g :
					gasit_loc = True
					break

			if gasit_loc:
				c.insert(i,s)
			else:
				c.append(s)

		
		
									
		