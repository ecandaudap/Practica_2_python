'''6. Escribe un script que detemine si un nombre dado por el usuario 
se encuentra en una lista de nombres. 
    La lista puede ser predeterminada o determinada por el usuario'''

lista_nombres = ['Raúl', 'Juan', 'Pedro', 'Felipe', 'Ana', 'Karla', 'Diana',
                 'Andrea', 'Andres', 'Nina', 'Carolina', 'Sergio', 'Paola',
                  'Paula', 'Rocío', 'Carmen', 'Ramón', 'Tina', 'Gabriela', 
                  'Armando', 'Diego', 'Rodrigo', 'Luis', 'Alfredo', 'Verónica']

nombre_usuario = input('Escribe un nombre para saber si esta en la lista: ')

if nombre_usuario in lista_nombres:
    print(f'{nombre_usuario} está en la lista')
else:
    print(f'{nombre_usuario} NO está en la lista')