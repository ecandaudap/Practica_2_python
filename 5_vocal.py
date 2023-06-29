'''5. Escribe un script que determine si una letra es vocal o no'''

letra = input('Escribe una letra: ')
letra_min = letra.lower()

if letra_min in 'aeiou':
    print(f'La letra {letra} es una vocal')
else:
    print(f'La letra {letra} es una consonante')


def function(number, kwarg = 3):
    
    
