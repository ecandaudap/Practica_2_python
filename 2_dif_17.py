'''2. Escribe un script que calcule 
la diferencia entre un número dado y 17 e imprima el resultado.
    Si el número es más grande que 17 deberá imprimir el doble de 
    la diferencia entre ambos números'''

numero = float(input('Ingrese un número: '))

if numero <= 17.0:
    diferencia = 17.0 - numero
    print(f'La diferencia entre {numero} y 17 es igual a {diferencia}')
else:
    diferencia = abs((17.0 - numero))*2
    print(f'El doble de la diferencia entre 17 {numero} es igual a {diferencia}')