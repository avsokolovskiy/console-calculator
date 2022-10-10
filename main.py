"""Simple calculator"""
import sys
def print_greetings():
    """Greetings function"""
    print('Hi pal! You are in the simple calculator 1.0.')


def print_instruction():
    """User manual function"""
    print('''
    Instruction: 
        1. Just follow the console prompts.
        2. To separate decimal part please use "."
        3. To quit, please enter "Q" and hit enter at any time.
    Happy calculations!
    ''')


def get_operand(number):
    """Getting operand from user"""
    while True:
        operand = input(f'Please input operand #{number}: ')
        calc_stop(operand)
        try:
            float(operand)
        except TypeError:
            print('Not a number. Please enter a valid number')
        else:
            if operand.isdigit():
                res_operand = int(operand)
            else:
                res_operand = float(operand)
            return res_operand



def get_operator():
    """Getting operator from user input"""
    while True:
        usr_operator = input('Please enter operator (supported operators +, -, *, /): ')
        calc_stop(usr_operator)
        if usr_operator in ('+', '-', '*', '/'):
            break

        print(f'The operator " {usr_operator} " is not supported')

    return operator


def calculation(operand_a, operand_b, akt_operator):
    """Function to perform calculation"""
    if akt_operator == '+':
        calc_result = operand_a + operand_b
    elif akt_operator == '-':
        calc_result = operand_a - operand_b
    elif akt_operator == '*':
        calc_result = operand_a * operand_b
    elif akt_operator == '/':
        calc_result = operand_a / operand_b
    return calc_result


def calc_stop(flag):
    """Function to exit calc"""
    if flag == "Q":
        print("Closing the simple calculator 1.0. See you!!!")
        sys.exit()


if __name__ == '__main__':
    print_greetings()
    print_instruction()
    while True:
        print('----------------------------------------------------------')
        operand_1 = get_operand(1)
        operand_2 = get_operand(2)
        operator = get_operator()
        if operand_2 == '0' and operator == '/':
            print('Division by zero is prohibited.')
        else:
            result = round(calculation(operand_1, operand_2, operator), 3)
            print(f'{operand_1} {operator} {operand_2} = {result}')
