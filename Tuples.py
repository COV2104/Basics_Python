x = tuple('stroka')
print(x)

x1 = (9, 8, 5, 6, 9, 3, 4, 5)
print(x1[5] + 10)
print(x1[2:5])


x2 = (9, 7, 3, 9, 4, 9, 1, 8)
y = []
for i in range(len(x2)):
    y.append(x2[i]+3)
print(x2)
print(y)
print(x2.count(9))


t = list(x2)
t[6] = 20
x2 = tuple(t)
print(x2)


n = (1, 2, 3)
m = n
n += (4, 5, 6)
b = n
print(n)
print(m)
print(b)
