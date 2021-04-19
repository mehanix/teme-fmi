
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
        out = open("{0}/{1}".format(output_folder,output_filename),"w")
        run(inp, out)
        inp.close()
        out.close()

def run(inp, out):
    """ Pregateste variabilele pentru testul cu datele din fisierul inp. Ruleaza algoritmii.

    Args:
        inp (IO): Fisier input
        out (IO): Fisier output
    """

    # citesc cheile din fisier
    key_strings = inp.readlines()
    key_strings = [s.strip() for s in key_strings]
    
    nr_incuietori = len(key_strings[0])
    for key in key_strings:
        if len(key) != nr_incuietori:
            print("Input error in fisierul {0}! Chei cu lungime diferita. ".format(inp.name))
            sys.exit(-1)
        for ch in key:
            if ch not in ['i','d','g']:
                print("Input error, caracter nerecunoscut in cheia: ",key)
                sys.exit(-1)

    # la inceput, toate incuietorile sunt inchise 1 data
    start = [Incuietoare(1) for x in range (nr_incuietori)]
    scopuri = [Incuietoare(0) for x in range (nr_incuietori)]
    
    Graph.keys = key_strings
    Graph.timeout = timeout
    Graph.nsol = nsol
    Graph.out = out
    NodParcurgere.out = out
    ucs(start,scopuri,out)
    a_star(start,scopuri,out,euristica="banala")
    a_star(start,scopuri,out,euristica="admisibila_1")
    a_star(start,scopuri,out,euristica='admisibila_2')
    a_star(start,scopuri,out,euristica="neadmisibila")
    a_star_v2(start,scopuri,out,euristica="banala")
    a_star_v2(start,scopuri,out,euristica="admisibila_1")
    a_star_v2(start,scopuri,out,euristica="admisibila_2")
    a_star_v2(start,scopuri,out,euristica="neadmisibila")
    ida_star(start,scopuri,out,euristica="banala")
    ida_star(start,scopuri,out,euristica="admisibila_1")
    ida_star(start,scopuri,out,euristica="admisibila_2")
    ida_star(start,scopuri,out,euristica="neadmisibila")

if __name__ == "__main__":
    main(sys.argv[1:])