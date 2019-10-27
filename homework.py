def sieve_of_erat():
    n = 10 ** 5 * 2
    a = list(range(n + 1))
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1
    print(lst[10000])


lst = [(i, j) for i in range(1, 7) for j in range(1, 7)]

a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0
a12 = 0
a13 = 0
a14 = 0
a15 = 0
a16 = 0
a23 = 0
a24 = 0
a25 = 0
a26 = 0
a34 = 0
a35 = 0
a36 = 0
a45 = 0
a46 = 0
a56 = 0
a125 = 0
a156 = 0
a256 = 0
for elem in lst:
    A1 = elem[0] % 2 == 0 and elem[1] % 3 == 0
    if A1:
        a1 += 1
    A2 = elem[0] % 3 == 0 and elem[1] % 2 == 0
    if A2:
        a2 += 1
    A3 = elem[0] % elem[1] == 0
    if A3:
        a3 += 1
    A4 = elem[1] % elem[0] == 0
    if A4:
        a4 += 1
    A5 = (elem[0] + elem[1]) % 2 == 0
    if A5:
        a5 += 1
    A6 = (elem[0] + elem[1]) % 3 == 0
    if A6:
        a6 += 1
    if A1 and A2:
        a12 += 1
    if A1 and A3:
        a13 += 1
    if A1 and A4:
        a14 += 1
    if A1 and A5:
        a15 += 1
    if A1 and A6:
        a16 += 1

    if A2 and A3:
        a23 += 1
    if A2 and A4:
        a24 += 1
    if A2 and A5:
        a25 += 1
    if A2 and A6:
        a26 += 1

    if A3 and A4:
        a34 += 1
    if A3 and A5:
        a35 += 1
    if A3 and A6:
        a36 += 1

    if A4 and A5:
        a45 += 1
    if A4 and A6:
        a46 += 1

    if A5 and A6:
        a56 += 1

    if A1 and A2 and A5:
        a125 += 1

    if A1 and A5 and A6:
        a156 += 1

    if A2 and A5 and A6:
        a256 += 1
print(a256)
