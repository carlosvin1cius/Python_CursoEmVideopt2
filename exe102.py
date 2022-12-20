def fatorial(n=1, show=0):
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True:
            print(f"{c} x ", end="")   
    print(f"= {f}")
fatorial(5, True)