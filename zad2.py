#coin-toss

import random

glava= 0
pismo= 0

for i in range(1000):
    palo = random.randint(1,2)   # 1-glava, 2-pismo

    if palo == 1:
        glava += 1

    else:
        pismo += 1

print("Pala glava: " + str (glava))
print("Palo pismo: " + str (pismo))