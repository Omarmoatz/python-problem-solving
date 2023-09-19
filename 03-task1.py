'''
function print multiplication table between x,y
'''
def mul_table(x,y):
    for nums in range(x,y+1):
        for num in range(10):
            print('-', num ,'*', nums ,'=', num*nums)
        print('________')

x=int(input('enter 1st number: '))
y=int(input('enter 2ed number: '))

print(mul_table(x,y))
