#prime_numer

def prime(n):
    aval=True
    for i in range(2, n):
        if n % i == 0:
            aval = False
    return aval

for i in range(2,100):
    if prime(i):
        pass
    else:
        print (i,end=", ")
c=6
print (c)


