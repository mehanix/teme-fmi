
sp_oriz = []
sp_vert = []
EPS = 1e-12 # eroare pt operatii cu floaturi

inf = float('inf')
with open("input.txt") as f:
    q = [float(x) for x in f.readline().split()]
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
    y_inf = -inf
    y_sup = inf

    for plan in sp_oriz:
        b = plan[0]
        c = plan[1]
        y_nou = - c / b

        if b > 0:
            if y_nou >= q[1] - EPS:
                y_sup = min(y_nou, y_sup)
        else:
            y_nou = - c / b
            if y_nou <= q[1] + EPS:
                y_inf = max(y_nou, y_inf)

    #vertical
    x_inf = - inf
    x_sup = inf

    for plan in sp_vert:
        a = plan[0]
        c = plan[1]
        x_nou = - c/a
        if a > 0: 
            x_nou = - c/a
            if q[0] - EPS <= x_nou: 
                x_sup = min(x_nou, x_sup)
        else: 
            x_nou = - c/a
            if x_nou <= q[0] + EPS: 
                x_inf = max(x_nou, x_inf)
    

    if x_inf != -inf and x_sup != inf and y_inf != - inf and y_sup != inf: 
        if x_inf < x_sup + EPS and y_inf < y_sup + EPS:
            print("exista un dreptunghi cu proprietatea ceruta.")
            val =  (x_sup - x_inf) * (y_sup - y_inf)
            print("valoarea minima a ariilor este: " + str(val))
        else:
            print("nu exista")
    else:
        print("nu exista")