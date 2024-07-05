class Game():  
    def __init__(self):
        while True:
            user_input = int(input('''Enter the game number
            1 - remove_duplicate
            2 - multiplication_table
            3 - divided_by
            4 - exit th game
            '''))
            if user_input == 1:
                self.remove_duplicate()

            elif user_input == 2:
                self.multiplication_table()

            elif user_input == 3:
                self.divided_by()
            
            elif user_input == 4:
                print('goodbye play again later')
                break

            else:
                print('invalid number please choose between 1 to 4')
            

            try_again_input = input('Do you want to paly again ?\nwrite yes to play again and no to exit the game : ')
            
            if try_again_input == 'yes':
                return Game()
            
            elif try_again_input == 'no':
                print('goodbye ........')
                break
            else:
                print('invalid input')
                break


    def remove_duplicate(self):
        sentence = input('enter your duplicated sentence : ')
        new_sentence = sentence.split(' ')
        result = []
        for word in new_sentence:
            if word not in result:
                result.append(word)
        final_sentence = ' '.join(result)
        print(final_sentence)

        
    def multiplication_table(self):
        x = int(input('Enter your first number : '))
        y = int(input('Enter your seconed number : '))
        for num1 in range(x, y+1):
            for num2 in range(1,11):
                print(f'{num1} * {num2} = {num1*num2}')
            print('------------------------')

    def divided_by(self):
        x = int(input('Enter your first number : '))
        y = int(input('Enter your seconed number : '))
        result = []
        for num in range(1,101):
            if num % x == 0 and num % y == 0:
                result.append(num)
        print(result)


    def __str__(self):
        return ""  # Return an empty string or a custom message

    def __repr__(self):
        return self.__str__()
        







print(Game())