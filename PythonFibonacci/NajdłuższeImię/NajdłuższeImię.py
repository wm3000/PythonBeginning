def odKońca(imię):
    nowe = ""
    for i in range(len(imię)):
        nowe += imię[-1-i]
    return nowe


print("Podaj imiona dziesięciu osób.")
max = 0;
maximię = ""
for i in range(4):
    imię = input("podaj imię: ")
    while not imię.isalpha():
        imię = input("podaj imię ponownie: ")
    ni = len(imię)
    if ni > max:
        max= ni
        maximię = imię
print("najdłuższe imię: ", maximię, " ma ", max, " znaków. Imię od końca to: ", odKońca(maximię))
