import random
chars = 'abcdefghijklmnopqrstuvyxz1234567890!@#$'

number = 3
number = int(number)

length = 8
length = int(length)

for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)






'''
2. Implementoni nje funksion 'def gjenero_password(): ...' qe kthen stringje, dhe ka keto veti:
    - sa here qe therritet, gjeneron nje password te ndryshem (idealisht, sepse mund te qelloje qe gjenerohet dy here i njejti password).
    - gjatesia e stringjeve te gjeneruar eshte 8.

Pra:
gjenero_password() -> '#avdExy0'
gjenero_password() -> '!u#1_?-B'
gjenero_password() -> '%43xKjIR'

Nje pakete qe do t'ju duhet per kete ushtrim eshte paketa 'random', qe mund ta importoni duke ekzekutuar ne
skriptin tuaj komanden 'import random'. (Mund te lexoni me shume ketu: https://docs.python.org/3/library/random.html)

Kjo pakete permban disa funksione, mes te cilave:

random.choice(<nje liste me elemente>).

Perdorni help(random.choice) per te kuptuar me mire se c'ben ky funksion, si dhe kujtoni operatoret qe kemi pare ne seancat e meparshme per listat dhe stringjet.
'''
