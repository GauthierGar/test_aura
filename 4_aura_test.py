
def ispalindrome(nombre):
    decomp = [0] * 6
    for i in range(5,-1,-1):
        decomp[i] = int( (nombre / (10**i)) )
        nombre = nombre - decomp[i]*(10**i)
    decomp.reverse()

    if decomp[0] == 0:
        decomp = decomp[1:]
    if decomp[0] == 0:
        decomp = decomp[1:]

    n = len(decomp)
    ok = True
    for i in range(int(n/2)):
        if decomp[i] != decomp[n-i-1]:
            ok = False
    return ok

nombres = [i for i in range(100,999+1)]

palindromes = []

n = len(nombres)
i = n - 1
i = 999

keep_going = True

while i > 99:
    j = i
    while j > 99:
        temp = i * j

        if ispalindrome(temp):
            #keep_going = False
            palindromes.append(temp)
        j = j -1
    i = i - 1

print(max(palindromes))


