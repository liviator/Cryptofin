import time
import random
finale = []
import math
import matplotlib.pyplot as plt

def one_two_attack(q, number_of_attack):
    
    #variable q = puissance de hashage relative de l'attaquant (0-0.5)
    #nombre d'attaque effectué 
    R = [] #Tableau recensant le nombre de block miné officielement par l'attaquant a chaque attaque
    H= [] #Tableau recensant le nombre de block miné par la blockchain officielle

    
    for i in range(number_of_attack):
        count_r = 0 #compte du nombre de block miné par l'attaquant dans cette attaque
        count_h = 0#compte du nombre de block miné par la blockchain principale dans cette attaque
        for j in range(3):
            result = random.uniform(0,1) #on choisit un nombre reel aléatoire entre 0 et 1
            if(j == 0):
                if result > q: #le nombre est supérieur à la puissance de hashage, la blockchain mine un bloc, fin de l'attaque (attaquant n'a pas miné le premier bloc)
                    count_h = 1
                    break     
                if result < q:
                    count_r = count_r+1
            else: #on compte le nombre de block ajouté à la blockchain de l'attaquant et ceux ajouté à celle officielle
                if result < q:
                    count_r = count_r+1
            if( j == 2):
                if(count_r == 3): #L'attaquant à miné 3 block, 3 blocks sont ajouté à la blockchain officielle
                    count_h = 3
                if(count_r == 2):#l'attaquant à miné 2 block, 2 blocks sont ajouté à la blockchain officielle
                    count_h = 2
                if(count_r == 1):#l'attaquant à miné 1 block, la blockchain officielle en a donc miné 2, l'attaquant n'a miné aucun block officiel
                    count_h = 2
                    count_r = 0         
        H.append(count_h)        
        R.append(count_r)
        ER = 0
        EH = 0
        for i in range(len(H)):
            ER = ER + (R[i])
            EH = EH + (H[i])
    finale = ER/EH #on fait le rapport pour toute l'attaque du nombre de block miné par l'attaquant par rapport aux nombres de block sur la blockchain principale 
    return finale
  
  
  
def simulation_double_spend():
    i=0
    result = []
    itération = 0
    premier_seuil = False
    N = int(input('Number of cycle'))
    a = int(input('Ecart toléré avec la blockchain principale'))
    z= int(input("Nombre de confirmation"))
    block_premine = int(input("Nombre de block préminé"))
    while(i < 0.5): #On effectue 275 attaque de N cycle avec une puissance de hashage incrémentée à chaque itération
        esperance = double_spending(N,a,z,block_premine,i)
        result.append(esperance)
        if(esperance > i):
            if(premier_seuil == False): #affiche la premiere puissance ou le rendement E[R]/E[H] > q
                print("Il a été rentable de miner avec une puissance de %f" % (i))
                premier_seuil = True
        i=i+0.002
        
    y_axis = tab(0.5,0.002)
    plt.plot(y_axis, result, label = "attacker ") #creation du plot
    plt.plot(y_axis,y_axis, label="honest mining")
    plt.xlabel('puissance de hashage')
    plt.ylabel('rendement')
    plt.show()
