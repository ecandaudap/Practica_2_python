'''5. Escribe un script que solicite un número y 
devuelva notifique al usuario si el número es par o impar'''

n = int(input('Dame un número entero para saber si es par o impar: '))

if n % 2 == 0:
    print(f'El número {n} es par')
else:
    print(f'El número {n} es impar')