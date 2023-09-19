'''
take sentence and word and remove the word from the sentence
'''
def remove_word(sentence,word):
    x= sentence.replace(word,' ')
    return x

x= input('enter the sentence: ')
y= input('enter the word you wnt to rwmove: ')

print(remove_word(x,y))


