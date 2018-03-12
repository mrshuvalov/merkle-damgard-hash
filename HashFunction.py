def todouble(x):
    x = str(bin(x))[2:]
    x = x.zfill(4)
    return x


def LS(x):

    arraydec = []
    for a in x:
        arraydec.append(int(a, 16))

    s = [11, 7, 9, 0, 8, 5, 12, 1, 2, 15, 3, 13, 14, 6, 10, 4]

    for a in range(len(arraydec)):
        for b in range(len(s)):
            if arraydec[a] == b:
                arraydec[a] = s[b]

    arraybin = []

    for a in arraydec:
        for b in todouble(a):
            arraybin.append(int(b))

    l = {0: 4, 8: 12, 16: 20, 24: 28, 1: 5, 9: 13, 17: 21, 25: 29, 2: 6, 10: 14, 18: 22, 26: 30, 3: 7, 11: 15, 19: 23, 27: 31}


    for a in range(len(arraybin)):
        for b in l:
            if a == b:
                arraybin[l[b]] = arraybin[a]


    b = ''
    c = ''
    for a in range(len(arraybin)):
        c += str(arraybin[a])
        if (a+1) % 4 == 0:
            b += str(hex(int(c, 2)))[2:]
            c = ''
    b = b.zfill(8)
    return b


def mod2(x, y):
    x_dec = int(x, 16)
    y_dec = int(y, 16)
    sum = str(hex(x_dec ^ y_dec))[2:]
    sum = sum.zfill(8)
    return sum

def d_func(i):
    global c
    i_string = str(i)
    i_string = i_string.zfill(8)
    d = mod2(c[i], LS(mod2(c[i], LS(i_string))))
    return d

def Fkx(x, k):
        return LS(mod2(x, k))

def key0(x, k):
    global c
    F = x
    for a in range(11):
        F = Fkx(F, d_func(a))
    k.append(mod2(d_func(11), F))


def keys(k):
    global c
    F = k[0]
    for a in range(1, 12):
        for b in range(11):
            F = Fkx(F, d_func(a))
        k.append(mod2(d_func(11), F))
        F = k[a]

def encryption(x, k):
    F = x
    for a in range(11):
        F = Fkx(F, k[a])
    return (mod2(k[11], F))


def hash_func(x, i, hash, k):
    hash.append(mod2(encryption(mod2(x, hash[i-1]), k), k[i]))

def hash_f(x):
    hash = []
    hash.append(IV)
    k = []

    key0(IV, k)
    keys(k)
    for a in range(1, 12):
        hash_func(x, a, hash, k)


    return hash[11]


IV = '2b838811'
c = ['8e20faa7', '2ba0b470', '47107ddd', '9b505a38', 'ad08b0e0', 'c3282d1c', 'd8045870', 'ef14980e', '6c022c38',
     'f90a4c07', '3601161c', 'f205268d']

