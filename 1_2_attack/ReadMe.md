# 1-2 Attack


Cette attaque repose sur une succession de 3 minage de block. Dans cette attaque, l'objectif est de miner davantage de block que la blockchain principale. Ainsi on analyse plusieurs scenarios possible :

Si la blockchain principale mine le premier block, l'attaque échoue comme l'attaquant n'a pas l'avantage de taille de chaine par rapport à celle officielle

Si il mine le premier block, l'attaque continue et se décline en 3 scenario (Ici R étant l'attaquant et H la blockchaine principale:

-L'attaquant mine les 3 blocs (R R R) : L'attaquant peut écraser la blockchain principale, gagner ses recompenses de minage et potentiellement recommencer son attaque
-L'attaquant mine 2 block (R H R ou R R H): il a toujours l'avantage du nombre de block sur la blockchain principale, il écrase et la blockchain principale avance de 2 blocks
-L'attaquant mine 1 block(R H H ) : La blockchain principale avance de 2 blocks, l'attaquant n'a aucune récompense 


Une fois l'attaque réalisé, on repertorie le nombre de block officiel issu par l'attaquant divisé par l'ensemble des blocks de la blockchain officielle, ce qui nous permet de determiner le rendement. 


Afin de représenter le taux de hashage minimum pour obtenir un rendement R > q avec q la puissance de hashage relative, une méthode effectue des successions de 15000 cycles d'attaque en utilisant une puissance de hashage croissante et en dresse un graphique. Ainsi, on peut s'appercevoir sur le graphique en annexe que la puissance minimum pour atteindre un seuil de retabilité par rapport à un mineur lambda est de q = 41% de puissance de hashage relatif.
