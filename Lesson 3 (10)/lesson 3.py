d = {1:2, 3:4, 5:6}
d[100] = 101
d[102] = [1,2,3,4,5]
d[0] = 99
for key, value in d.items():
    print(key, value)
print(d.get(0, -1))
d.update({1:5, 7:4})
print(d)