#za dati broj vratiti listu pozicija na kojima se pojavljuje u proslijedjenom nizu

niz=[1,2,3,4,5,3,7,7]
broj=3
pozicije=[]

for i in range(len(niz)):

    if niz[i] == broj:
        pozicije.append(i)

print(pozicije)