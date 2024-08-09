# tuple is same as list but only you can't add or remove items from tuple

nums = (1, 2, 3, 4)
print(type(nums))

if 3 in nums:
    print('exists')

result = [num for num in nums if num <=3 ]

print(result)

# ------------------------------------------------------------
# (a, b) == a, b     --> i can define a tuple without using brackets 

a = 10
b = 15

# c = a
# a = b
# b = c

a , b = b , a

print(a,b)
