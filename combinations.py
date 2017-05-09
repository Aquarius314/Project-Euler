def combinations(number):
    combs = []  # to w Pythonie deklaracja nowej tablicy
    for n in number:    # petla foreach dla wszystkich znaczkow w liczbie
        new_combs = []  # tablica po nowej iteracji
        for c in combs: # foreach dla kazdej kombinacji z poprzedniej iteracji
            for i in range(len(c)+1):   # petla dla kazdego miejsca w danej kombinacji
                new_combs.append(c[0:i]+n+c[i:len(c)])  # dodajemy nowa kombinacje z literka
        combs = new_combs   # podmieniamy liste kombinacji na nowe

        if len(combs) == 0: # jesli lista kombinacji jest pusta, dodajemy pierwszy znak
            combs.append(n)
    combs = sorted(combs)
    return combs

C = combinations("0123456789")

print(C[999999])
