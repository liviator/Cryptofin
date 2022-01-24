### Minage Optimal


## Variable 

Ce programme agit en fonction de plusieurs paramètre, a le nombre de block la blockchain de l'attaquant, h le nombre de block de la blockchai officielle, n le nombre de block ciblé pour la simulation, c le cout et q la puissance de hashage relative et renvoie le gain maximal du joueur en fonction des paramètres.

## Concept

Ce programme a pour but de simuler le gain maximal d'un joueur qui part de la position a h et s'arrete à (0,0), durant la partie, le joueur va être confronté à diverses situation dépendant de l'état de a et h. Il sera ainsi amené à chosir entre attendre un block suivant (l'équivalent d'un lancer de piece), écraser la blockchain principale (en abandonnant ou non) ou abandonner 

Action écraser : Le joueur révèle ses blocs et devient la blockchain officielle, afin de réaliser cette action, il doit avoir un nombre de block supérieur ou égal à h+1. Suite à l'action écraser, si il a toujours plus de block que la blockchain princiaple (a>h+1), alors h retourne à 0 et a à la valeur a-h-1, il peut alors continuer son action. Si cela n'est pas le cas, l'action écraser mettra fin à son minage.

Action attendre: Le joueur décide d'attendre le block suivant, block qui pourra être miné soit par lui soit par la blockchain officiel 

action abandonner: le joueur peut être contraint à abandonner dans le cas ou h>a


Ainsi en prennant en compte ses actions et en calculant via recursivité depuis l'état initial de l'esperance (à n=0), nous pouvons obtenir le gain que peut gagner un joueur lorsqu'il effectue cette technique


L'image ci-contre représente une simulation avec les paramètre a = 0, h = 0 et n = 13, le cout ainsi que la puissance de hashage étant variable
![image](https://user-images.githubusercontent.com/76626503/150873725-93cb1e97-28e1-4018-925c-5f5be2e6a7da.png)



Cette image représente la simulation avec les paremètre a=0,h=0 et n=3 (paramètre de l'attaque 1-2), on peut s'appercevoir que le mineur n'a de gain qu'a partir du seuil préalablement défini dans l'attaque 1-2 (q>0,414)

![image](https://user-images.githubusercontent.com/76626503/150868900-09e56b6a-dad2-4b7e-aaba-667d94cadc04.png)
