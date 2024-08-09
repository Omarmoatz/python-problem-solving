# genarator: its used in iterations(loop) as it generate a value 
#            to use then don't store it in the memory then 
#            generate the next value to use and don't store it and so on
#            - its much faster than ordinary list comprehension
#            - only used in large numbers of data 

from sys import getsizeof   # measures with bytes

gen = (x*2 for x in range(1000000))
print(getsizeof(gen))  

for item in gen:
    print(list(gen))


my_list = [x*2 for x in range(1000000)]
print(getsizeof(my_list)) 