'''5. Escribe un script que solicite un número y 
devuelva notifique al usuario si el número es par o impar

opción 1
validar que solo acepte números y volver a pedir el valor
'''

continuar = True

while continuar:
    n = input('Ingrese número entero para saber si es par o impar: ')

    try:
        entero = int(n) #intentamos la conversión
        if entero % 2 == 0:
            print(f'El número {entero} es par')
        else:
            print(f'El número {entero} es impar')
        
        continuar = isinstance(entero,(bool, str, float))
    except (ValueError):
        print("El dato ingresado no es número entero, vuelva a intentarlo")
        print("")
        continuar = isinstance(n,(bool, str, float))

    
    
