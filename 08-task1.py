'''
take x, y and print all nums divded by y from x to 100
'''
def divided_by(x,y):
    numbers=[]
    for nums in range(x,101):
        if nums%y == 0 :
            numbers.append(nums)
    return numbers

x = int(input('Enter 1st number: '))
y= int(input('Enter 2ed number: '))

print(divided_by(x,y))


