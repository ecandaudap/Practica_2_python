'''9 Escribe un script que imprima si un string dado por el usuario
contiene números o no'''

caracteres = input('Escribe una cadena de caracteres: ')

for i in range(0,len(caracteres)):
    if caracteres[i] in '0123456789':
        print('El string contiene números')
        break
    elif i == len(caracteres)-1:
        print('El string NO contiene números')
    


