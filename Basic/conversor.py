def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " tienes? ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares.")


menu = """
Bienvenido al conversor de monedas:
1.-Pesos Colombianos.
2.-Pesos Chilenos.
3.-Pesos Argentinos.

Elige una opción: 
"""

opcion = int(input(menu))

if opcion == 1:
    conversor('Colombianos', 3875)
elif opcion == 2:
    conversor('Chileno', 750)
elif opcion == 3:
    conversor('Argentinos', 65)
else:
    print("Debes elegir una opción")
