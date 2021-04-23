import copy
import time

class NodParcurgere:
    out = None
    gr = None
    def __init__(self, info, g, parinte, key=None, h=0):
        self.info=info
        self.parinte=parinte #parintele din arborele de parcurgere
        self.g=g #acesta este costul
        #pt a*
        self.h = h
        self.f = self.g + self.h
        #end pt a*

        self.key = key #cheia care a fost aplicata pt a obtine acest nod (sau None pt nod start)

    def obtineDrum(self):
        l=[self]
        nod=self
        while nod.parinte is not None:
            l.insert(0, nod.parinte)
            nod=nod.parinte
        return l
        
    def afisDrum(self,ida_max=None): #returneaza si lungimea drumului
        global max_ida
        stop_time = time.time()
        l = self.obtineDrum()
        chei = [x.key for x in l]
        lg = len(l)
        for i in range(lg):
            NodParcurgere.out.write("{0}) {1}\n".format(i,repr(l[i])))
            if i != lg-1:
                NodParcurgere.out.write("Folosim cheia: [" + repr(chei[i+1]) + "] pentru a ajunge la...\n")

        NodParcurgere.out.write("\nStare scop: " + "".join(repr(l[-1])) +'\n')
        NodParcurgere.out.write("\n------------\nStats:\n")
        NodParcurgere.out.write("Lungime drum: " +str(lg-1) +'\n')
        NodParcurgere.out.write("Cost drum: " +str(lg-1) +'\n')
        NodParcurgere.out.write("Timp gasire solutie: " +str(round(1000*(stop_time - Graph.start_time))) +'ms\n')

        maxim = Graph.maxim if ida_max is None else ida_max
        NodParcurgere.out.write("Nr noduri maxim existente in memorie: " +str(maxim) +'\n')
        NodParcurgere.out.write("Nr total noduri calculate: " +str(Graph.noduriTotale) +'\n')
        return len(l)


    def contineInDrum(self, infoNodNou):
        nodDrum=self
        # print(infoNodNou, nodDrum.info, infoNodNou == nodDrum.info)
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
    noduriTotale = 0
    start_time = 0
    timeout = 0
    keys = []
    nsol = 0
    maxim = 0
    def __init__(self, start, scopuri, euristica: str = "banala"):
        self.euristica = euristica
        self.start=start
        self.scopuri=scopuri
        Graph.noduriTotale = 0
        Graph.maxim = 0
        Graph.start_time = time.time()

    def testeaza_scop(self, nodCurent):
        return nodCurent.info == self.scopuri

    
    def genereazaSuccesori(self, nodCurent):
        """Genereaza succesori.

        Aplicand lui nodCurent o cheie obtin o alta stare.
        Costul aplicarii unei chei este 1.
        Determin toate starile in care se poate merge din nodul nodCurent.

        Args:
            nodCurent (NodParcurgere): Nodul unde ma aflu momentan in arbore

        Returns:
            [NodParcurgere]: Lista succesorilor nodului curent.
        """

        listaSuccesori=[]
        for key in Graph.keys:
            incuietori = copy.deepcopy(nodCurent.info)
            infoNodNou = Graph.apply_key(incuietori, key)
            if not nodCurent.contineInDrum(infoNodNou):
                listaSuccesori.append(NodParcurgere(infoNodNou, g = nodCurent.g + 1, parinte = nodCurent, key = key, h= self.calculeaza_h(infoNodNou)))


        Graph.noduriTotale += len(listaSuccesori)
        return listaSuccesori
        

    def calculeaza_h(self, nod):
        if self.euristica == "banala":
            if nod != self.scopuri:
                return 1
            return 0
        if self.euristica == "admisibila_1":
            return max([x.get() for x in nod])
        if self.euristica == "admisibila_2":
            return min([x.get() for x in nod])
        if self.euristica == "neadmisibila":
            return sum([x.get() for x in nod])
        return 0


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
        