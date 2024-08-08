
nums = list(range(21))

even_nums = nums[::2]
reverse_nums = nums[::-1]

# print(even_nums)
# print(reverse_nums)
  

# ------------------------------------------------------------
# ___updating , unpacking_list____

letters = ['a', 'b', 'c', 'd', 'f', 'a','a','a']

for index , value in enumerate(letters):
    # print(index, value)
    pass

# print(letters.index('b'))
# print(letters.count('a'))

letters.append('ed')
letters.insert(2, 'cd')
letters.pop(1)
letters.remove('f')
del letters[0]
# letters.clear()
# print(letters)


# ------------------------------------------------------------
# ___sorting___

numbers = [2, 8, 4, 1, 0, 6, 10]

# print(sorted(numbers,reverse=True)) # create new list and put sorted values in it
numbers.sort(reverse=True)
# print(numbers)

# ------------------
teams = [
    ('team2', 10),
    ('team1', 50),
    ('team5', 80),
    ('team3', 40),
    ('team4', 35)
]

def teamsfunc(teams):
    return teams[1]

teams.sort(key=teamsfunc, reverse=True)
# print(teams)


items = [
    ('item2', 10),
    ('item1', 50),
    ('item5', 80),
    ('item3', 40),
    ('item4', 35)
]

points = list(map( lambda item: item[1], items))
print(points)

filtered = list(filter( lambda item: item[1] <= 40, items))
print(filtered)


