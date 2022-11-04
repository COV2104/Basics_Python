from itertools import count


def show():
    print('функция')


show()


def show2():
    x = 7
    return x+10


y = show2()
z = show2() + 10
print(y)
print(z)
show()


def count_list(par, count=0):
    for i in par:
        count += 1
    return count

f = [1,9,7,6,3,4,8,5]
print(count_list(f))
j=['a', 'e', 'q', 'c']
print(count_list(j))
n=[5,6,3,7,8,1,55,1,2,35]
print(count_list(n))


def exclusive_item(*args):
    new_list = []
    for i in args:
        for j in i:
            if j not in new_list:
                new_list.append(j)
    return new_list

x = [1,8,9,2,65,47,55,55,23,77,2]
f = [1,2,2,8,56,55,4,5,78,77,23,2]
d = [5,7,8,5,6,9,3,4,5,6,2,1,7,7,7,23,55,47,6]

t = exclusive_item(x,f,d)
print(t)
