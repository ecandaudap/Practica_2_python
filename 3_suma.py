'''3. Escribe un script que calcule la suma de 3 números dados 
por el usuario.
    Si los valores son iguales deberá imprimir la suma multiplicada por 3
'''

print('Ingrese 3 números \t')
n1 = float(input('numéro 1: '))
n2 = float(input('numéro 2: '))
n3 = float(input('numéro 3: '))

if (n1 == n2) & (n2 == n3):
    suma = (n1 + n2 + n3)*3
    print(f'El triple de la suma de {n1}, {n2} y {n3} es igual a {suma}')
else:
    suma = n1 + n2 + n3
    print(f'La suma de {n1}, {n2} y {n3} es igual a {suma}')