# Dictionary: same as list but its assigened with key, value

dictinary = {'x':17, 'y':10}
new_dict = dict(z=20, a=30)

print(new_dict)

dictinary['b'] = 25
print(dictinary)

del dictinary['b']
print(dictinary)

print(new_dict.get('v', 'not found'))

for key , value in new_dict.items():
    print(key, value)

# ---------------------------------------------------
# list_comprehenion

points = {x: x*2 for x in range(10)}
print(points)
