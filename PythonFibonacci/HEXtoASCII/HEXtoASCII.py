
text = input()
z1 = int(text[0])
z2 = text[1]
if z1 > 1 and z1 < 8:
    if z2 >= 'A' and z2 <= 'F':
        dec = int(text[0] + text[1], 16)
        print(str(dec))
        print(chr(dec))
    else:
        print('złe dane wejściowe')
else: 
    print('złe dane wejściowe')
