'''
2- create a function takes 2 nums and print all nums
 between 1 and 100 that can be diveded by x , y  
'''
def divided_by(x,y):
    numbers=[]
    for nums in range(100):
        if nums%x == 0 and nums%y == 0 :
            numbers.append(nums)
    return numbers

x = int(input('Enter 1st number: '))
y= int(input('Enter 2ed number: '))

print(divided_by(x,y))

