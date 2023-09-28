Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

#1
def listupper():
    newNames=[]
    for name in Names:
        newNames.append(name.upper())
    return newNames

def listComperihension():
    return[ name.upper() for name in Names]

def myUpper(n):
    return n.upper()

ELBolbol=list(map(myUpper,Names))
#_________________________________________________________________________
#2

def containsA():
    newNames=[]
    for name in Names:
        if 'a' in name:
            newNames.append(name)
    return newNames

def listcom():
    return[name for name in Names if 'a' in name]

def myfilter(n):
    if 'a' in  n:
        return True

funPro=list(filter(myfilter,Names))
#__________________________________________________________
#3

def startT():
    listOfT=[]
    for name in Names:
        if name[0] == 't' :
            listOfT.append(name)
    return listOfT

def listcomp():
    return[name for name in Names if name[0]=='t']

def myfilt(n):
    if n[0] == 't':
        return True

funcpro=list(filter(myfilt,Names))
#__________________________________________________________
#4
def contain2aORmore():
    newList=[]
    for name in Names:
        if name.count('a') >= 2:
            newList.append(name)
    return newList

def listcomper():
    return[name for name in Names if name.count('a')>=2]

def fltr(n):
    if n.count('a') >= 2:
        return True
fpro=list(filter(fltr,Names))
#___________________________________________________________
#5
def wordLength():
    leght=[]
    for name in Names:
        leght.append(len(name))
    return leght

def listcomperh():
    return[len(name) for name in Names ]

def fun_pro(n):
    return len(n)

funproo=list(map(fun_pro,Names))
#__________________________________________________________
#7
a, *b = Names
print(f"""
a = {a}
b = {b}
""")

#8
a , *_ , b = Names
print(f"""
a = {a}
b = {b}
""")

#9
a,b,*_=Names
print(f"""
a = {a}
b = {b}
""")
