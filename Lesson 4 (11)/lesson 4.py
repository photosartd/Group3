def bubble_sort(l):
    for i in range (len (l)):
        for j in range (len (l) - i - 1):
            if l[j] > l [j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
g = [2,4 ,1 ,0]
bubble_sort(g)
print(g)