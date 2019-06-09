import pygame

while int(input('dane czujnika: ')) != 0:
    print('czekam na 0')

licznik = 0
pop = 0
zm = int(input('dane czujnika: '))
while zm != -1:    
    if zm > 0 and zm != pop:
        licznik += 1
    pop = zm
    zm = int(input('dane czujnika: '))


print('licznik=', licznik)
