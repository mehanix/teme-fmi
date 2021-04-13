
import sys, getopt
from pathlib import Path

def main(argv):
    input_folder = ''
    output_folder = ''
    nsol = -1
    timeout = -1
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
    
    assert timeout != -1
    assert nsol != -1
    assert Path(input_folder).is_dir()
    assert Path(output_folder).is_dir()

if __name__ == "__main__":
    main(sys.argv[1:])