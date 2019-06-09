print('nowy projekt przeliczanie sekund na minuty, godziny')

sek = int(input())
minuty = int(sek / 60)
godziny = int(minuty/60)
print(str(godziny % 24) + 'h' + str(minuty%60) + 'm' + str(sek%60) + 's')

