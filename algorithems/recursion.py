# Recursion: its function which calls it self many times until it reaches base case
#             - use it only in nessary
#             - it use stack for storing runing functions 


def factorial(num):
    if num <= 1:    # base case
        return 1
    else:           # recursive case
        return num * factorial(num-1)

def main():
    return factorial(4)

print(main())