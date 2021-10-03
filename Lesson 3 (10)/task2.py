def merge_dicts(dct1, dct2):
    new_d = {}
    for key in dct1.keys():
        if key in dct2:
            new_d[key] = max(dct1[key], dct2[key])
            del dct2[key]
        else:
            new_d[key] = dct1[key]
    new_d.update(dct2)
    return new_d

d1 = {'a':1, 'b':2}
d2 = {'a':3, 'c':4}
print(merge_dicts(d1, d2))