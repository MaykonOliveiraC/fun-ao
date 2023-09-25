def contador(i, f, p):
    c = i
    while c <= f:
        print(f"{c}", end='..')
        c += p
    print("Fim!")


contador(0, 100, 10)