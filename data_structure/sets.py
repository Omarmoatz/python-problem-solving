# Sets : same as list but all elements in sets is unique as they don't duplicate
#           also can use some math with it as union, diffrence, intersection, symetric diffrence
#           also it can't be indexed 

numbers = [1, 2, 3, 4, 5]
first = set(numbers)
seconed = {4, 5, 6, 7, 8}

first.add(6)
first.remove(6)
print(first)

print(first | seconed) # union: all elements in first, seconed
print(first & seconed) # intersection: elements in first and seconed
print(first - seconed) # diffrence: elements in first and not inseconed
print(first ^ seconed) # symetric diffrence: revese of intersection

# seconed[1] = 10   error --> it can't be indexed

if 3 in first:
    print('exists')


points = {x*2 for x in range(10)}
print(points)