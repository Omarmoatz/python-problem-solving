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

'''
3 function print multiplication table between x,y
'''
def mul_table(x,y):
    for nums in range(x,y+1):
        for num in range(10):
            print('-', num ,'*', nums ,'=', num*nums)
        print('________')

x=int(input('enter 1st number: '))
y=int(input('enter 2ed number: '))

print(mul_table(x,y))

'''
4 remove duplicate
'''
def remve_duplicate(sentence):
    new_sentence=[]
    for word in sentence.split(' '):
        if word not in new_sentence:
            new_sentence.append(word)
        else: continue
    return new_sentence

x=input('Enter the sentence: ')

print(remve_duplicate(x))

'''
5 ake sentense and print how many words in  it 
'''
def count_words(sentence):
    new_sentence=[]
    new_sentence.append(sentence.split(' '))
    x= sum(len(n) for n in new_sentence)
    return x

x= input('enter the sentence: ')

print(count_words(x))

'''
6 take sentence and word and remove the word from the sentence
'''
def remove_word(sentence,word):
    x= sentence.replace(word,' ')
    return x

x= input('enter the sentence: ')
y= input('enter the word you wnt to rwmove: ')

print(remove_word(x,y))

'''
7 takes sen, word how many times word used in sentence
'''
def count_word(sentence,word):
    return sentence.count(word)

x= input('enter the sentence: ')
y= input('enter the word: ')

print(count_word(x,y))

'''
8 take x, y and print all nums divded by y from x to 100
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