#____with_lists____
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]

values = *list1, 12,45, 'k', *list2

print(*list1)
print(*values)
 
#____with_dicts____
dict1 = {'x':10, 'y':20}
dict2 = {'z':15, 'a':25, 'x':12}

all_dicts = {**dict1, 'omar':22, **dict2}
print(all_dicts)