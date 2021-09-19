#1
print('Hello world')
#2
a = 2
print(type(a))
#3
if True:
    print('True')
else:
    print('False')
#4 cycles
i = 0
while i < 10:
    print(i)
    i += 1
for i in range(1, 10, 2):
    print(i)

#5 strings
s = 'Dima'
print(s)
print(len(s))

#arrays (lists)
names = ['Timur', 'Ivan', 'Sonya']
for name in names:
    print(name)

l2 = list('Timur')
print(l2)
print(l2[0:3])
#Неизменяемость строк
s = 'Dima'
print(s[0]) #D
l2[0] = 'L'
print(l2)
l2.append('e')
l2.append('s')
print(l2)
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[1][1])
l3 = [1, 2]
l4 = [3, 4]
l3.insert(1, 7)
l5 = list(range(10))
print(l5)
l5.insert(0, 10)
print(l5)
len(l5)