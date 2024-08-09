# stack 
# lifo  == last in first out

web_history = []

web_history.append('link_web1')
web_history.append('link_web2')
web_history.append('link_web3')
print(web_history)

# go back 
web_history.pop()
print(f'redirecting to {web_history[-1]}')
print(web_history)

# go back 
web_history.pop()
print(f'redirecting to{web_history[-1]}')
print(web_history)

# go back 
web_history.pop()
if not web_history:
    print('your web history is empty')
