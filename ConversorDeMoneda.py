def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")


menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige que moneda desea convertir en USD: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3435)
elif opcion == 2:
    conversor("argentinos", 83)
elif opcion == 3:
    conversor("mexicanos", 20)
else:
    print('Ingresa una opción correcta por favor')
