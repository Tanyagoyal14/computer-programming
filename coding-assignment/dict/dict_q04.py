d = {'a': 1, 'b': 2, 'c': 3}


k, val = 'd', 4

target = 'b'


res = {}

for key, value in d.items():
    
    
    res[key] = value
    
    if key == target:
        res[k] = val

print(res)
