import copy
#informatii despre un nod din arborele de parcurgere (nu din graful initial)
class NodParcurgere:
	def __init__(self, info, cost, parinte, key=None):
		self.info=info
		self.parinte=parinte #parintele din arborele de parcurgere
		self.g=cost #acesta este costul
		self.key = key #cheia care a fost aplicata pt a obtine acest nod (sau None pt nod start)
	def obtineDrum(self):
		l=[self]
		nod=self
		while nod.parinte is not None:
			l.insert(0, nod.parinte)
			nod=nod.parinte
		return l
		
	def afisDrum(self): #returneaza si lungimea drumului
		l = self.obtineDrum()
		chei = [x.key for x in l]
		lg = len(l)
		for i in range(lg):
			print("{0}) {1}".format(i,repr(l[i])))
			if i != lg-1:
				print("Folosim cheia: [", chei[i+1], "] pentru a ajunge la...")

		print("\nStare scop:", "".join(repr(l[-1])))
		print("Numar chei folosite:",lg-1)
		return len(l)


	def contineInDrum(self, infoNodNou):
		nodDrum=self
		while nodDrum is not None:
			if(infoNodNou==nodDrum.info):
				return True
			nodDrum=nodDrum.parinte
		
		return False
		
	def __repr__(self):
		sir = ""
		if self.key is None:
			sir+="Initial: "
		else:
			sir= "Incuietori: "
		sir += "".join(repr(self.info))
		return(sir)
		

class Graph:
	"""Graful efectiv al problemei
	"""

	# variabila statica
	keys = []

	def __init__(self, keys, start, scopuri):
		self.start=start
		self.scopuri=scopuri

	def testeaza_scop(self, nodCurent):
		return nodCurent.info == self.scopuri

	
	def genereazaSuccesori(self, nodCurent):
		"""Genereaza succesori.

		Aplicand lui nodCurent o cheie obtin o alta stare.
		Costul aplicarii unei chei este 1.
		Determin toate starile in care se poate merge din nodul nodCurent.
		Am grija sa nu merg in cerc (adaug doar starile care nu au aparut deja in drum).

		Args:
			nodCurent (NodParcurgere): Nodul unde ma aflu momentan in arbore

		Returns:
			[NodParcurgere]: Lista succesorilor nodului curent.
		"""

		listaSuccesori=[]

		for key in Graph.keys:
			incuietori = copy.deepcopy(nodCurent.info)
			incuietori = Graph.apply_key(incuietori, key)

			# daca am ajuns pe o stare intalnita anterior, o ignoram, ca sa nu facem bucla
			# if nodCurent.contineInDrum(incuietori):
			# 	continue
			listaSuccesori.append(NodParcurgere(incuietori,nodCurent.g + 1, nodCurent, key))

		return listaSuccesori
		

	def apply_key(incuietori, key):
		"""Foloseste o cheie pe incuietoare.

		Args:
			incuietori ([Incuietoare]): Starea curenta a lacatului
			key (string): Cheia

		Returns:
			[Incuietoare]: Starea lacatului dupa folosirea cheii.
		"""
		res = copy.deepcopy(incuietori)
		for i in range(len(key)):
			ch = key[i]
			if ch == 'i':
				res[i].update(1)
			elif ch == 'd' and res[i].get() > 0:
				res[i].update(-1)
		#print("Aplic", key,incuietori, " Rezulta: ", res)
	
		return res


	def __repr__(self):
		sir=""
		for (k,v) in self.__dict__.items() :
			sir+="{} = {}\n".format(k,v)
		return(sir)
		
		

##############################################################################################	
#                                 Initializare problema                                      #
##############################################################################################		

def ucs(start, keys, scopuri, nsol):

	Graph.keys = keys
	gr = Graph(keys, start, scopuri)
	uniform_cost(gr,nsol)


#### algoritm Uniform Cost Search
#presupunem ca vrem mai multe solutii (un numar fix)
#daca vrem doar o solutie, renuntam la variabila nrSolutiiCautate
#si doar oprim algoritmul la afisarea primei solutii


def uniform_cost(gr, nrSolutiiCautate=1):

	# Initializez cu configuratia de start (toate incuietorile pe 1)
	c = [ NodParcurgere(gr.start, 0, None) ]
	
	while len(c)>0:
		#print(c)
		# input()
		
		# iau element curent
		nodCurent=c.pop(0)
		
		# daca e solutie, afisam si scadem nr de solutii
		if gr.testeaza_scop(nodCurent):
			print("nrsolcaut",nrSolutiiCautate)
			print("Solutie: ")
			nodCurent.afisDrum()
			print("\n----------------\n")
			nrSolutiiCautate-=1
			input()
			
			if nrSolutiiCautate==0:
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

		
		
									
		