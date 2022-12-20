def score(dice):
     #une déclare une variable "somme"
    somme = 0
    #une déclare une variable "p1" qui prend comme valeur le nombre de répétitions de "1" dans la liste 'dice'
    #on utilise la fonction count qui nous permet de compter le nombre de répétitions de l'argument dans la liste
    p1 = dice.count(1)
    #une déclare une variable "p5" qui prend comme valeur le nombre de répétitions de "5" dans la liste 'dice'
    p5 = dice.count(5)
    #ici on vérifie si le nombre de répétitions de "1" dans la liste 'dice' est supérieuer ou égal à '3'
    if p1 >= 3:
         #si la condition est vérifiée  :on soustrait '3' du 'p1' et on ajoute '1000' à 'somme' car d'après la consigne 'Three 1's => 1000 points'
       p1 -= 3
       somme += 1000
       #ici on ajoute la multiplication de "100*p1" (en utilisant la valeur de p1 après la soustraction) à 'somme' car ( One   1   =>  100 points) donc si après la soustraction on a p1=2 on va faire "100*2"
    somme += 100 * p1
    #ici on vérifie si le nombre de répétitions de "5" dans la liste 'dice' est supérieuer ou égal à '3'
    if p5 >= 3:
         #si la condition est vérifiée  :on soustrait '3' du 'p5' et on ajoute '500' à 'somme' car d'après la consigne 'Three 5's => 500 points'
       p5 -= 3
       somme += 500
        #ici on ajoute la multiplication de "50*p5" (en utilisant la valeur de p5 après la soustraction) à 'somme' car ( One   5   =>  50 points),par exemple: si après la soustraction on a p5=2 on va faire "50*2"
    somme += 50 * p5
    #on vérifie si le nombre de répétitions de '6'est supérieur ou égal à '3'
    if dice.count(6) >= 3:
         #si la condition est vérifié on ajoute '600' à 'somme' car 'Three 6's =>  600 points' sinon on ajoute rien
         somme += 600
     #on vérifie si le nombre de répétitions de '4'est supérieur ou égal à '3'
    if dice.count(4) >= 3:
         #si la condition est vérifié on ajoute '400' à 'somme' car 'Three 4's =>  400 points' sinon on ajoute rien
         somme += 400
     #on vérifie si le nombre de répétitions de '3'est supérieur ou égal à '3'
    if dice.count(3) >= 3:
         #si la condition est vérifié on ajoute '300' à 'somme' car 'Three 3's =>  300 points' sinon on ajoute rien
         somme += 300
     #on vérifie si le nombre de répétitions de '2'est supérieur ou égal à '3'
    if dice.count(2) >= 3:
         #si la condition est vérifié on ajoute '200' à 'somme' car 'Three 2's =>  200 points' sinon on ajoute rien
         somme += 200
     #on retourne la valeur de 'somme'
    return somme
