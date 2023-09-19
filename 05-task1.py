'''
take sentense and print how many words in  it 
'''
def count_words(sentence):
    new_sentence=[]
    new_sentence.append(sentence.split(' '))
    x= sum(len(n) for n in new_sentence)
    return x

x= input('enter the sentence: ')

print(count_words(x))
