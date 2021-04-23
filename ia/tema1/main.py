
import sys, getopt, os
from src.incuietoare import Incuietoare
from src.ucs import ucs
from src.graph import Graph, NodParcurgere
from src.a_star import a_star
from src.a_star_v2 import a_star_v2
from src.ida_star import ida_star

nsol = -1
timeout = -1

def main(argv):
    """ Incarca, parseaza datele de intrare, verifica corectitudinea lor.

    Args:
        argv (list): lista argumentelor pasate in command-line.
    """
    global nsol,timeout
    input_folder = ''
    output_folder = ''

    try:
        opts, args = getopt.getopt(argv, "i:o:n:t:")
    except getopt.GetoptError:
        print('main.py -i <input_folder> -o <output_folder> -n <nr_solutii> -t <timeout>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-i":
            input_folder = arg
        elif opt == "-o":
            output_folder = arg
        elif opt == "-n":
            nsol = int(arg)
        elif opt == "-t":
            timeout = int(arg)
        else:
            print("Argument error")
            sys.exit(2)
    
    if timeout == -1 or nsol == -1 or not os.path.isdir(input_folder):
        print("Argument error")
        sys.exit(2)

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    
    for filename in os.listdir(input_folder):
        output_filename = "output_" + filename
        inp = open("{0}/{1}".format(input_folder, filename),"r")
        out_ucs = open("{0}/{1}_ucs".format(output_folder,output_filename),"w")
        out_astar = open("{0}/{1}_astar".format(output_folder,output_filename),"w")
        out_astar_v2 = open("{0}/{1}_astar_v2".format(output_folder,output_filename),"w")
        out_idastar = open("{0}/{1}_idastar".format(output_folder,output_filename),"w")

        run(inp, out_ucs,out_astar,out_astar_v2,out_idastar)
        inp.close()
        out_ucs.close()
        out_astar.close()
        out_astar_v2.close()
        out_idastar.close()

def run(inp, out_ucs,out_astar,out_astar_v2,out_idastar):
    """ Pregateste variabilele pentru testul cu datele din fisierul inp. Ruleaza algoritmii.

    Args:
        inp (IO): Fisier input
        out (IO): Fisier output
    """

    # citesc cheile din fisier
    key_strings = inp.readlines()
    key_strings = [s.strip() for s in key_strings]
    
    # verificarea corectitudinii datelor de intrare
    nr_incuietori = len(key_strings[0])
    for key in key_strings:
        if len(key) != nr_incuietori:
            print("Input error in fisierul {0}! Chei cu lungime diferita. ".format(inp.name))
            sys.exit(-1)
        for ch in key:
            if ch not in ['i','d','g']:
                print("Input error, caracter nerecunoscut in cheia: ",key)
                sys.exit(-1)

    # verific daca problema e fara solutii
    exista_d = [0 for x in range(nr_incuietori)]
    for key in key_strings:
        for i,ch in enumerate(key):
            if ch == 'd':
                exista_d[i]=1
    
    #daca exista incuietori pe care nicio cheie nu le poate deschide => problema fara solutii
    if sum(exista_d) != nr_incuietori:
        for out in [out_ucs,out_astar,out_astar_v2,out_idastar]:
            out.write("Input fara solutii!")
            out.close
        return

    # la inceput, toate incuietorile sunt inchise 1 data
    start = [Incuietoare(1) for x in range (nr_incuietori)]
    scopuri = [Incuietoare(0) for x in range (nr_incuietori)]
    
    Graph.keys = key_strings
    Graph.timeout = timeout
    Graph.nsol = nsol

    print("hi")
    ucs(start,scopuri,out_ucs)
    print("hi")

    for eur in ["banala","admisibila_1","admisibila_2","neadmisibila"]:
        a_star(start,scopuri,out_astar,euristica=eur)
        a_star_v2(start,scopuri,out_astar_v2,euristica=eur)
        ida_star(start,scopuri,out_idastar,euristica=eur)

if __name__ == "__main__":
    main(sys.argv[1:])