'''
1 function that takes 2 nums and print a list containing odd and even nums in this range
'''
def odd_even_nums(x,y):
    even_nums=[]
    odd_nums=[]
    for nums in range(x,y+1):
        if nums%2 == 0 :
            even_nums.append(nums)
        else:
            odd_nums.append(nums)
    return even_nums , odd_nums
    
x=int(input('enter 1st number: '))
y=int(input('enter 2ed number: '))

even,odd=odd_even_nums(x,y)
print('odd nums are : ' , odd)
print('even nums are : ' , even)








