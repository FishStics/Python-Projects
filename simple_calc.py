import time
#simple calculator, can add, subtract, multiply, or divide two numbers


def numbers():
    num_one = int(input('enter the first number: '))
   
    num_two = int(input('enter the second number: '))
    
    def calculate():
        print('would you like to add, subtract, multiply, or divide the numbers? (enter as a, s, m, or d)')
        
        equation = input()
        
        if equation == 'a':
            print(num_one + num_two)
        
        elif equation == 's':
            print(num_one - num_two)
        
        elif equation == 'm':
            print(num_one * num_two)
        
        elif equation == 'd':
            print(num_one % num_two)
        
        else:
            print('please enter a, s, m, or d.')
            time.sleep(0.5)
            calculate()
        
        print('would you like to calculate something else? (yes, no)')
        again = input()
        
        if again == 'yes':
            numbers()
        
        else:
            print('okay, goodbye!')
        
    calculate()


numbers()