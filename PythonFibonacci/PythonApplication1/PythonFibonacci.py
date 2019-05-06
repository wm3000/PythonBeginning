print("test - fibonacci")

a, b = 0, 1
while a < 10000000:
    if a==0: print(a)
    else: print(str(a) + ' proporcja=' + str(b/a))
    a, b = b, a+b

