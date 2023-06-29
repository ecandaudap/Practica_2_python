'''5. Escribe un script que solicite un número y 
devuelva notifique al usuario si el número es par o impar

opción 1
validar que solo acepte números y volver a pedir el valor
'''

continuar = True

while continuar:
    n = input('Ingrese número entero para saber si es par o impar: ')
    
    if n.isdigit() == False:
        print("El dato ingresado no es número entero, vuelva a intentarlo")
        print("")
        continuar = isinstance(n,(bool, str, float))
    else:
        n = int(n)

        if n % 2 == 0:
            print(f'El número {n} es par')
        else:
            print(f'El número {n} es impar')
        
        continuar = isinstance(n,(bool, str, float))
    
    


