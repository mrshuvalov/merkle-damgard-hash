import HashFunction

msg = input("Введите сообщение в 16-ричном виде: ")

x = []
y = ''

m = len(msg) % 8
if m > 0:
    for a in range(len(msg) - m):
        if (a + 1) % 8 == 0:
            x.append(msg[a-7: a+1])
    x.append(msg[len(msg) - m: len(msg) + 1].zfill(8))
elif m == 0:
    for a in range(len(msg)):
        if (a + 1) % 8 == 0:
            x.append(msg[a-7: a+1])
elif m == len(msg):
    x.append(msg.zfill(8))

for a in x:
    y += str(HashFunction.hash_f(a))

print(y)