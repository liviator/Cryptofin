# Double Spending Attack

## Principe

Dans cette attaque, l'attaquant va effectuer et une transaction malveillante et vas tenter de générer une chaine plus longue que la blockchain officielle pendant suffisament de block pour passer le seuil z selon une transaction est considéré comme valide

## Variable

L'attaque fonctionne via pusieurs paramètres. Le taux de hashage relatif q, le nombre d'attaque N , le nombre de confirmation z qui correspond au seuil de sécurité pour lequel une transaction devient valide, le nombre maximum d'écart avec la blockchain a ainsi que le nombre de block préminé. On considère généralement ce nombre comme étant égal à 1.

L'output correspond au rendemenent de la strategie i.e l'esperance du nombre de bloc miné officiellement par le mineur / l'esperance du nombre de bloc miné sur la blockchain principale.


## Le code

Concernant l'explication du code, se référer au fichier Double_Spending qui est commenté



## La simulation 


Voici le graphe issu d'une simulation en prennant comme variable N = 10000, a = 3, z = 10 et 1 block préminé, le rendement étant en fonction de q, cette donnée est variable et non prédéfinie 

La ligne jaune correspond au comportement d'un mineur honnete tandis que la courbe bleue celui d'un mineur malhonnete, la courbe est exponentielle et dans ce cas précis, il est rentable d'être malhonnete en obtenant environ 41% de puissance de hashage relatif
![image](https://user-images.githubusercontent.com/76626503/150856011-cea20ea6-e15d-45f4-951b-a14f5f150f4c.png)
