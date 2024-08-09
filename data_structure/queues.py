# Queue 
# fifo == first in first out
# I should use deque() because when i remove the first element in queue if shifts all 
#       the other elements to the left and this well make my programe more slower 

from collections import deque

my_queue = deque([])

my_queue.append('omar')
my_queue.append('shahd')
my_queue.append('aesha')

print(my_queue)

my_queue.popleft()
print(my_queue)
my_queue.popleft()
print(my_queue)
my_queue.popleft()

if not my_queue:
    print('your queue is empty')
