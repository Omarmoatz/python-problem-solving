'''
remove duplicate
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


