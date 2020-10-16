# # Buenas practicas; siempre definir una funcion principal que corra el programa desde el principio, run o main se consideran estandar en la industria.
#       def run():
#           pass
# 
#   Linea de entrada;
#       if __name__ == '__main__':
#           run
#   indica a python el inicio del programa
# 
# 
# Siempre se deben de dejar 2 espacios entre funciones y entre la linea de entrada, se considera el estilo oficial del lenguaje
def palindromo(palabra):
    palabra = palabra.replace(' ' , '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()