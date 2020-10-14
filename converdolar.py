dolares = input("¿Cuantos dolares tienes?: ")
dolares = float(dolares)
valor_pesos = 1/21
pesos = dolares / valor_pesos
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos")
