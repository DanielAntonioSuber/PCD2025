import string
import random

minusculas_ascii = string.ascii_lowercase
mayusculas_ascii = string.ascii_uppercase
numeros = string.digits

def generar_password(n):
    password = []
    
    for _ in range(n):
        opt = random.randint(1, 3)
        
        if opt == 1:
            password.append(random.choice(minusculas_ascii))
        elif opt == 2:
            password.append(random.choice(mayusculas_ascii))
        elif opt == 3:
            password.append(random.choice(numeros))
    
    return ''.join(password)


for i in range(10, 20):
    print(generar_password(i))