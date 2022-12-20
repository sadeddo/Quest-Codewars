def monkey_count(n):
    #on a initialisé une variable i qui prend comme valeur initiale 1 car notre conte par 1
    i=1
    #on initialise une liste vide
    monkey=[]
    while  i<= n:
        monkey.append(i)
        i=i+1
    return monkey
#on a utilisé la fonction append dans une boucle pour ajouter les valeur de i dans la liste 'monkey' 
#et i prend tous les chiffres entre 1 et n inclu
