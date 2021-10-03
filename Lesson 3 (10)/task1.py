q = list(input())
def dc(l):
    d = {}
    for elem in l:
        d[elem] = elem
    return d
a = dc(q)
print(a)