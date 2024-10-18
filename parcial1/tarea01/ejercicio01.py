
import string

caracteres_ascii = string.ascii_letters
print(caracteres_ascii)

def verificar(cadena):
    # Escribe el codigo que verifique que todos los caracteres de una
    # cadena son letras ASCII
    # Devuelve: True en caso de que todos los caracteres sean letras ascii
    #           False en caso contrario
    for caracter in cadena:
        if caracter not in caracteres_ascii:
            return False
    return True


cadena1 = "Esto es un a cadena$"
print(verificar(cadena1))