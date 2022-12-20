#nous avons ici quatre fonctions "unite", "dizaine", "centaine", "millier"
#qui prends en parametre  un entier b (pour la position de la fonction)
# une chaine de caractère str1
# et une second chaine de caractere (pour ajouter a chaque fois les caracteres au chiffre romain)
#les quatre fonctions ont la même facon de fonctionner
def unite(b , rom, str1):
    #a prend la valeur de la position des unité
    a = int(str1[b])
    #si c'est inferieur a 4 on va afficher a chaque fois I
    if a < 4:
        i = 0
        while i < a:
            rom += "I"
            i += 1
    #si c'est egal a 4 on va affivher IV (sachant que 4 et 9 son des cas particulier)
    elif a == 4:
        rom += "IV"
    #si c'est entre 4 et 9 on va afficher V(5) puis I a chaque pis
    elif 9 > a > 4 :
        rom += "V"+ ("I" * (a - 5))
    #si c'est egal a 9 on va afficher IX
    elif a == 9:
        rom += "IX"
    return rom
#se fonctionnement est le même pour toutes les autres fonctions il y a juste les caractère qui change

def dizaine(b, rom, str1):
    a = int(str1[b])
    if a < 4:
        i = 0
        while i < a:
            rom += "X"
            i += 1
    elif a == 4:
        rom += "XL"
    elif 9 > a > 4:
        rom += "L"+ ("X" * (a - 5))
    elif a == 9:
        rom += "XC"
    return rom
def centaine(b, rom, str1):
    a = int(str1[b])
    if a < 4:
        i = 0
        while i < a:
            rom += "C"
            i += 1
    elif a == 4:
        rom += "CD"
    elif 9 > a > 4:
        rom += "D"+ ("C" * (a - 5))
    elif a == 9:
        rom += "CM"
    return rom
def millier(b,rom,str1):
    a = int(str1[b])
    if a < 4:
        i = 0
        while i < a:
            rom += "M"
            i += 1
    elif a == 4:
        rom += "M(V)"
    elif 9 > a > 4:
        rom += "(V)"+ ("M" * (a - 5))
    elif a == 9:
        rom += "M(X)"
    return rom
#fonction principale
def solution(n):
    #on va d'abord convertir l'entier en chaine de caractere
    str1 = str(n)
    rom = ''
    #on va prendre la longueur de la chaine de caractere
    long = len(str1)
    #selon la longueur les unites, dizaines, centaines ... vont avoir une position differente
    if long == 1:
        rom = unite(0,rom,str1)
    elif long == 2:
        rom = dizaine(0,rom,str1)
        rom = unite(1,rom,str1)
    elif long == 3:
        rom = centaine(0,rom,str1)
        rom = dizaine(1,rom,str1)
        rom = unite(2,rom,str1)
    elif long == 4:
        rom = millier(0,rom,str1)
        rom = centaine(1,rom,str1)
        rom = dizaine(2,rom,str1)
        rom = unite(3,rom,str1)
    return rom
