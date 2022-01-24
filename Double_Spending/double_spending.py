def double_spending( N, a, z,block_premine, q): 
    #q = puissance de hachage relative
    #z = nombre de confirmation
    #a = ecart toléré avec la chaine honnete
    #N nombre d'attaque
    E_Mined = 0
    E_Official = 0
    for attack in range(N): #on repete l'attaque N fois
        blockchain_honnete = 0
        block_attack = block_premine #Pour qu'il y ait une attaque, un nombre de bloc doit etre au préalable miné
        block_diff = 0
        is_true = True
        while(is_true == True):
            result = random.uniform(0,1) #On tire un nombre al"atoire et on observe si il est inférieur ou supérieur à notre puissance de hashage relative ce qui nous permet de determiner qui a miné le bloc
            if result < q:
                block_attack = block_attack+1
            else:
                blockchain_honnete = blockchain_honnete + 1
            if block_attack >= z: #Tant qu'on a pas atteints le nombre de confirmation on continue d'attaquer
                E_Official = E_Official + block_attack
                E_Mined = E_Mined + block_attack
                break
            else:
                block_diff = blockchain_honnete - block_attack #Le minage est interrompu si la blockchain principale double l'attaquant d'un nombre a block 
                if block_diff >= a: 
                    E_Official = E_Official  + blockchain_honnete
                    break
    E_Official = E_Official / N
    if(E_Mined > 0):
        E_Mined = E_Mined / N
    return E_Mined/E_Official # retourne le rendement moyen de l'attaque
  
  
  def simulation_double_spend(): #Methode pour afficher sur un graphe le rendement par rapport à la puissance de hashage, les paramètres pouvant être modifié 
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
