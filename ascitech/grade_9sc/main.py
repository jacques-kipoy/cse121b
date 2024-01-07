from random import shuffle# imort random
print("n'importe quoi ")
mot = input("1")
mot1 = input("2")
mot2 = input("3")

c = []#liste vide
c.append(mot)# append mot soit importé dans la liste c
c.append(mot1)
c.append(mot2)
longueur = 3
nb_mdp = 5

def mdp(longueur):
    mdp = str()
    shuffle(c)#pour rangé et cjoisir aleatoirement
    for x in range(longueur):
        mdp += c[x]
    print(mdp)
for x in range(nb_mdp):
    mdp(longueur)