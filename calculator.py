def  calculator():
    def add(x, y):
        return x + y


    def subtract(x, y):
        return x - y


    def multiply(x, y):
        return x * y


    def divide(x, y):
        return x / y

    def power(x,y):
        return x**y

    promt = ('''
    please choose between operators:
    "+","-","*","/","**"
    ''')

    user_options = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '**': power
    }

    while True:
        operation = input(promt)
        num1 = float(input(" please enter a first number: "))
        num2 = float(input(" please enter a second number: "))
        print('_' * 12)

        if operation in user_options:
            selected_function = user_options[operation]
            print('Your result is: ', selected_function(num1, num2))
        else:
            print('un known command')



def root_of_2():
    num1=('please enter a number: ')
    epsilon=0.01
    guess=num1/2.0
    while abs(guess*guess-num1)>=epsilon:
        guess=guess-((guess**2)-num1/(2*guess))
        print('Square root of ', num1, 'is', guess)


def deg():
    degr, nummer = input("Enter cos, sin or tan and then the number: ").split()
    degr = degr.lower()
    import math
    if degr == "cos":
        result = math.cos(math.radians(int(nummer)))
        print(f'Your resalt  of cos is { result}')

    elif degr == "sin":
        result = math.sin(math.radians(int(nummer)))
        print(f'Your result  of sin is { result}')

    elif degr == "tan":
        result = math.tan(math.radians(int(nummer)))
        print(f'Your result  of tan is { result}')

    else:
        print("Something went wrong.")

def menu():
    user_command=input('Pleass choose the calculation between: calculator,square root, degrees or q to quit: ').lower()
    while user_command != 'q':
        if user_command == "calculator":
            calculator()
        elif user_command == "square root":
            root_of_2()
        elif user_command == "degrees":
            deg()
        else:
            pass

menu()



