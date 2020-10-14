def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")



menu = """ 
Bienvenido al conversor de monedas 💰
1- Pesos mexicanos
2- Pesos colombianos
3- Pesos chilenos

Elige una opcion: 
"""

opcion = input(menu)

if opcion == "1":
    conversor("mexicanos", 21)
elif opcion == "2":
    conversor("colombianos", 3836)    
elif opcion == "3":
    conversor("chilemos", 798.80)
else:
    print("Ingresa una opcion correcta por favor")


