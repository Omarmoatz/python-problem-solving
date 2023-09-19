'''
takes sen, word how many times word used in sentence
'''
def count_word(sentence,word):
    return sentence.count(word)

x= input('enter the sentence: ')
y= input('enter the word: ')

print(count_word(x,y))


