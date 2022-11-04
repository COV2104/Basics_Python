from re import A
from unittest import result


print('Lets go!')

number = 5
number2 = 6
result = number+number2
print(result)

num1 = num2 = 10
print(num1, num2)

num_1, num_2 = 3, 7
print(num_1, num_2)

swap1 = 9
swap2 = 10
swap1, swap2 = swap2, swap1
print(swap1, swap2)

a = 5
b = 3
a, b = b, a+b
print(a, b)

z, x, c = [1, 2, 3]
print(z, x, c)

z, x, *c = [1, 2, 3, 4, 5]
print(z, x, c)
