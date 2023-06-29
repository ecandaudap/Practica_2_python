'''8. Escribe un script que convierta una cantidad de segundos 
dada por el usuario a horas, minutos y segundos.
'''

print('Vamos a determinar el número de horas, minutos y segundos que hay \nen una cierta cantidad de segundos')
intro_seg = int(input('Escribe una cantidad de segundos: '))

horas = intro_seg // 3600
min = (intro_seg % 3600) // 60
seg = (intro_seg % 3600) % 60

print(f'{intro_seg} segundos equivale a {horas} horas, {min} minutos y {seg} segundos')