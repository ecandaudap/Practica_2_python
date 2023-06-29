'''1. Escribe un script que le pregunte al usuario varios nombres 
hasta que el usuario especifique que ya no desea ingresar más nombres.
    
    Como resultado deberá mostrar al usuario una lista, 
    una tupla y un set con todos los nombres que ingresó el usuario'''


lista_nombres = []

continuar = True

while continuar:
    nombres = input('Ingresa un nombre hasta que des enter para parar: ')
    if nombres == "":
        continuar = False
    else:
        lista_nombres.append(nombres)

tupla_nombres = tuple(lista_nombres)
set_nombres = set(lista_nombres)

print("")
print("La lista de nombres ingresados es:", lista_nombres)
print("")
print("La tupla de nombres ingresados es:", tupla_nombres)
print("")
print("El conjunto de nombres ingresados es:", set_nombres)