import time
import random
finale = []
import math
import matplotlib.pyplot as plt

def tab(nombre, increment):
    i=0
    tab = []
    while i<= nombre:
        tab.append(i)
        i = i+increment
    return tab

def strategie_optimale(a,h,n,q,c): #calcul du gain maximal du mineur au cours d'un cycle dont le but est de miner n bloc
    #h longueur blockchain principale
    #n nombre de bloc ciblé pour un cycle d'attaque
    #a blockchain attaquant
    #c cout
    #q puissance de hashage de l'attaquant
    if n == 0 :
        if a>h:
            return a - (a-h) *c
        else:
            return 0
    else:
        if (a > h+1 ): # cas : écraser ou attendre
            z = max(h+1-c + strategie_optimale(a-h-1,0,n,q,c), q * strategie_optimale(a+1,h,n-1,q,c) + (1-q) * (strategie_optimale(a, h+1, n-1,q,c) - c))
            return z
        if a == h+1 : #cas écraser (fin de cycle) ou attendre
            z = max(h+1-c,q * strategie_optimale(a+1,h,n-1,q,c) + (1-q) * (strategie_optimale(a,h+1, n-1,q,c)-c))
            return z
        if a <= h: #cas fin de cycle ou attendre
            z = max(0,q*strategie_optimale(a+1,h,n-1,q,c) + (1-q) * (strategie_optimale(a,h+1,n-1,q,c) - c))
            return z
          
          
          
 def simulation_optimale():
    n = int(input('Nombre de block '))
    h = int(input('longueur de la chaine principale '))
    a = int(input("longueur de la chaine de l'attaquant "))
    itération = 0
    result = []
    i=0
    while(i < 0.5):
        esperance = strategie_optimale(a,h,n,i,i)
        result.append(esperance)
        i=i+0.005
    y_axis = tab(0.5,0.005)
    plt.plot(y_axis, result, label = "attacker ") #creation du plot
    plt.plot(y_axis,y_axis, label="honest mining")
    plt.xlabel('puissance de hashage')
    plt.ylabel('rendement')
    plt.show()
       
