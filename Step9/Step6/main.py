def is_triangle(a, b, c):
    x = a+b
    y = a+c
    z = b+c
    #si la somme de deux cotés est inferieur ou égal au troisieme coté ce n'est pas un triangle
    if (x <= c) or (y <= b) or (z <= a):
        return False
    else:
        return True
