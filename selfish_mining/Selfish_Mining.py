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


def selfish_mining(q, N, gamma):
    #q puissance de hashage relative
    #gamma correspond au ratio de mineur qui vont miner sur la pool de l'attaquant 
    H= 0 #Nombre de block de la blockchain officielle
    R= 0 #Nombre de block miné par l'attaquant

    for i in range(N):
        j=0
        blockchain_honnete = 0
        block_attack = 0
        block_diff = 0
        while(True):
            result1 = random.uniform(0,1) 
            if(j == 0): #l'attaque commence si l'attaquant mine un block
                if result1 > q:
                    H= H+1
                    break
                else:
                    j=1
                    block_attack = block_attack+1
            else: #On fait une simulation de qui mine le block entre l'attaquant et les honnetes mineurs
                if result1 > q:
                    blockchain_honnete = blockchain_honnete + 1
                else:
                    block_attack = block_attack+1
                block_diff = blockchain_honnete - block_attack #On calcule la différence entre la chaine de l'attaquant et la chaine honnete
                if block_diff == 0 : #Les deux chaines font la meme taille
                    result2 = random.uniform(0,1) #On tire un random pour savoir si les mineurs vont miner à partir de la chaine de l'attaquant ou celle honnete
                    if(result2<=gamma):
                        R = R+block_attack
                        H = H+block_attack+1
                        break
                    else:
                        H= H+ blockchain_honnete + 1
                        break
                elif block_diff == 1: #La chaine honnete est plus longue et devient officielle
                    H = H + blockchain_honnete
                    break
                elif block_diff == -1: #la chaine malhonnette est plus longue et devient officielle
                    R = R+block_attack
                    H = H+block_attack
                    break


    Blockchain_officielle = H / N
    Nb_block_mine_attaquant = R/N
    return Nb_block_mine_attaquant / Blockchain_officielle #on calcul le rendement
  
  
def simulation_selfish():
    N = int(input("Nombre d'attaque"))
    itération = 0
    result1 = []
    result2 = []
    result3 = []
    i=0
    while(i < 0.5):
        rendement1 = selfish_mining(i,N,0)
        rendement2 = selfish_mining(i,N,0.5)
        rendement3 = selfish_mining(i,N,1)
        result1.append(rendement1)
        result2.append(rendement2)
        result3.append(rendement3)
        
        i=i+0.005
        
    y_axis = tab(0.5,0.005)
    plt.plot(y_axis, result1, label = "attacker ") #creation du plot
    plt.plot(y_axis, result2, label = "attacker ")
    plt.plot(y_axis, result3, label = "attacker ")
    plt.plot(y_axis,y_axis, label="honest mining")
    plt.legend(['gamma=0','gamma=0.5','gamma=1',"honnest Miner"])
    plt.xlabel('puissance de hashage')
    plt.ylabel('rendement')
    plt.show()
    
