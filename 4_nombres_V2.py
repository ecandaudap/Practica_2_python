'''4. Escribe un script que calcule cuantas veces se repite 
un nombre en una lista de nombres determinada por el usuario.'''

lista_nombres = []

continuar = True

while continuar:
    nombres = input('Ingresa un nombre hasta que des enter para parar: ')
    if nombres == "":
        continuar = False
    else:
        lista_nombres.append(nombres)

set_nombres = set(lista_nombres)

for nombre in set_nombres:
     conteo = lista_nombres.count(nombre)
     print(f'El nombre {nombre}, se repite {conteo} veces')