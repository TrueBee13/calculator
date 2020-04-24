# calculator
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


'''
def root_of_2(num1):
  epsilon=0.01
  guess=num1/2.0
  while abs(guess*guess-num1)>=epsilone:
    guess=guess-((guess**2)-num1/(2*guess))
    print('Square root of ', num1, 'is', guess)
'''

promt = ('''
please choose between operators:
to add numbers press 1,
to subract - 2,
to multiply - 3,
to divide - 4,
find a sqyare root of real numer - 5
''')

user_options = {
    1: add,
    2: subtract,
    3: multiply,
    4: divide
}

while True:
    operation = int(input(promt))
    num1 = float(input(" please enter a first number: "))
    num2 = float(input(" please enter a second number: "))
    print('_' * 12)

    if operation in user_options:
        selected_function = user_options[operation]
        print('Your result is: ', selected_function(num1, num2))
    else:
        print('un known command')

    # operation=int(input(promt))







