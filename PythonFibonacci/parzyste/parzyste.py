a = int(input())
b = int(input())

indeks = a
while indeks <= b:
    if indeks%2 == 0:
        print(indeks)
    indeks += 1

for a in range(b):
    if a%2 == 0:
        print(a)