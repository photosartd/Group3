print('List comprehension: ')
l = ['k', 'i', 'n']
print(l)

a = [i for i in range(5, 25) if i % 2 == 0]
print(a)

print("Итерация по списку: ")
for elem in l:
    print(elem)

print('Кортежи: ')
d = (1,2,3, 'Sir')
#d[0] = 4 - ошибка


#функции

def get_list(l:list, x):
    a = []
    for elem in l:
        if elem < x:
            a.append(elem)
    return a

def better(l, x):
    return [elem for elem in l if elem < x]


nums = [345,463,32356, 1, 3,5]
x = 4
res = better(nums, x)
print(res)

