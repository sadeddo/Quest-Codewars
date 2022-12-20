def basic_op(operator, value1, value2):
    if operator == '+':
        a= value1 + value2
    elif operator == '-':
        a= value1 - value2
    elif operator == '*':
        a= value1 * value2
    elif operator == '/':
        a= value1  / value2
    else:
        print("Choose one of the following operator:+,-,*,/")
    return a
#on a utilisé if et elif pour verifier le signe mathématique qu'on a stocker dans la variable 'operator' et faire les calculs avec le signe correspondant
