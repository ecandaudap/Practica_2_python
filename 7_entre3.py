'''7. Escribe un script que le pida al usuario un número mínimo y un número máximo de un rango de números.
    El script debe imprimir cuales de ellos son divisibles entre 3'''

print("Vamos a acoptar un segmento de línea recta de números enteros: ")
n_inf = int(input('Escribe el número entero inferior: '))
n_sup = int(input('Escribe el número entero superior: '))
print('')
print('Los números divisibles entre 3 son:')

for n in range(n_inf, n_sup+1, 1):
    if n % 3 == 0:
        print(f'El {n}')
    else:
        #print(f'El {n} NO es divisible entre 3')
        continue