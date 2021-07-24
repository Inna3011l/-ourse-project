f = open('1.txt')
s = 0
n = 0
for i in f:
    print(i)
    print(len(i))
    g = int(i[len(i) - 2])
    s = +8
    n += 1
    if g < 3:
        print(i[:-1])

    print(s/n)    