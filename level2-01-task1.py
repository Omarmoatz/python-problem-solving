Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
#1
def uppercase(name):
    new=[]
    for word in Names:
        new.append(word.upper())
    print(new)
print(uppercase(Names)) 

def upper(name):
    return [ word.upper() for word  in Names] 

print(upper(Names))

UPP= list(map(str.upper, Names))
print(UPP)

#2
def a(name):
    NEW = []
    for x in name:
        if 'a' in x:
            NEW.append(x)
    return NEW
print(a(Names))

def aa(name):
    return [i for i in name if 'a' in i]
print(aa(Names))

def aaa(name):
    if 'a' in name:
        return name
#3

def t(name):
    new = []
    for x in name:
        if x[0] == 't':
            new.append(x)
        continue
    return new
print(t(Names))


def tt(items):
    return [i for i in items if i[0] == 't']
print(tt(Names))

def ttt(word):
    if word[0] == 't':
        return word

tttt = list(filter(tt, Names))
print(tttt)

#4
def word_has2A(name):
    new = []
    for i in name:
        if i.count('a') >= 2:
            new.append(i)
    return new
print(word_has2A(Names))


def word_has2A_4(name):
    return [i for x in name if x.count('a') >= 2]
print(word_has2A_4(Names))

def  chek_word_has2A_4(word):
    if word.count('a') >= 2:
        return word

chek_word_has2A_4a = list(filter(chek_word_has2A_4, Names))
print(chek_word_has2A_4a)

#5
def task_5(items):
    len_list = []
    for i in items:
        len_list.append(len(i))
    return len_list
print(task_5(Names))


def list_comprehension_5(items):
    return [len(i) for i in items]
print(list_comprehension_5(Names))

functional_programming_5 = list(map(len, Names)) 
print(functional_programming_5)
