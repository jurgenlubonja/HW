def prodhimi(A):
    p = A[0]
    for numer in A[1:]:
        p *= numer

    return p


print(prodhimi([1,2,3]))
print(prodhimi([1,2]))
print(prodhimi([1,2,0]))
print("---------")


numri0, numri1, numri2 = 1, 2, 3
numri3 = 0,
lista_fillestare = [numri0, numri1, numri2, numri3]
lista_perfundimtare = list(reversed(lista_fillestare))

# Ne kete rast output do te jet nje liste me numrin 0 e printuar 6 here sepse ne kete rast variabli "numri3" eshte tuple dhe jo integer
#sepse eshte vendosur , mbas 0.Per te rregulluar kodin ne menyre qe te dali output 0 thjesht duhet te heqim ,

#print(lista_fillestare)
#print(lista_perfundimtare)

print(prodhimi(lista_perfundimtare))