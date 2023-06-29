'''5. Escribe un script que solicite un número y 
devuelva notifique al usuario si el número es par o impar

opción 2
que pregunte si quiere ingresar más números a evaluar, si la respuesta es negativa
entonces que termine el programa
'''
""

continuar = True

while continuar:
    n = int(input('Dame un número entero para saber si es par o impar: '))

    if n % 2 == 0:
        print(f'El número {n} es par')
    else:
        print(f'El número {n} es impar')

    answer = input('¿Quieres ingresar más números? (y/n)')

    if answer in ['n', 'N']:
        break
    


