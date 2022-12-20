def square_digits(num):
    #on transforme num en chaine de caracteres 
    a = str(num)
    #un caractere vide
    b = ""
    for i in a:
        b += str(int(i)**2)
    return int(b)
#on a parcouru les caracteres de a et apres les transformer en chiffre *2


