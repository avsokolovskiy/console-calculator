"""Simple calculator"""
import sys
from typing import TypeVar

Typecalc = TypeVar('Typecalc', int, float)


def print_greetings() -> None:
    """Greetings function"""
    print('Hi pal! You are in the simple calculator 1.0.')


def print_instruction() -> None:
    """User manual function"""
    print('''
    Instruction: 
        1. Just follow the console prompts.
        2. To separate decimal part please use "."
        3. To quit, please enter "Q" and hit enter at any time.
    Happy calculations!
    ''')


def get_operand(number: str) -> str:
    """Getting operand from user"""
    while True:
        operand = input(f'Please input operand #{number}: ')
        calc_stop(flag=operand)
        try:
            float(operand)
        except ValueError:
            print('Not a number. Please enter a valid number')
        else:
            return operand


def get_operator() -> str:
    """Getting operator from user input"""
    while True:
        usr_operator = input('Please enter operator (supported operators +, -, *, /): ')
        calc_stop(flag=usr_operator)
        if usr_operator in ('+', '-', '*', '/'):
            break

        print(f'The operator " {usr_operator} " is not supported')

    return usr_operator


def calculation(operand_a: str, operand_b: str, akt_operator: str) -> Typecalc:
    """Function to perform calculation"""
    return eval(f'{operand_a}{akt_operator}{operand_b}')


def calc_stop(flag: str) -> None:
    """Function to exit calc"""
    if flag == "Q":
        print("Closing the simple calculator 1.0. See you!!!")
        sys.exit()


if __name__ == '__main__':
    print_greetings()
    print_instruction()
    while True:
        print('----------------------------------------------------------')
        oprnd_1 = get_operand(number='1')
        oprnd_2 = get_operand(number='2')
        oprtr = get_operator()
        if oprnd_2 == '0' and oprtr == '/':
            print('Division by zero is prohibited.')
        else:
            result = round(calculation(operand_a=oprnd_1, operand_b=oprnd_2, akt_operator=oprtr), 3)
            print(f'{oprnd_1} {oprtr} {oprnd_2} = {result}')
