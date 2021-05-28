sp_oriz = []
sp_vert = []
EPS = 1e-12 # eroare pt operatii cu floaturi

with open("input.txt") as f:
    # citesc si separ planurile in orizontale/verticale
    n = int(f.readline())
    for i in range(n):
        r = f.readline().split()
        [a, b, c] = [int(x) for x in r]

        if a == 0:
            sp_oriz.append((b,c))
        else:
            sp_vert.append((a,c))

    # orizontal
    y_inf = -float('inf')
    y_sup = float('inf')

    for plan in sp_oriz:
        b = plan[0]
        c = plan[1]
        y_nou = - c/b
        if b > 0:
            y_sup = min(y_nou, y_sup)
        else:
            y_inf = max(y_nou, y_inf)

    # vertical
    x_inf = -float('inf')
    x_sup = float('inf')

    for plan in sp_vert:
        a = plan[0]
        c = plan[1]
        x_nou = - c/a

        if a > 0:
            x_sup = min(x_nou, x_sup)
        else:
            x_inf = max(x_nou, x_inf)

    if x_sup < x_inf  or y_sup < y_inf:
        print("intersectie vida")
    else:
        if x_inf != -float('inf') and x_sup != float('inf') \
            and y_inf != -float('inf') and y_sup != float('inf'):
            print("intersectie nevida marginita")
        else:
            print("intersectie nevida nemarginita")
    
