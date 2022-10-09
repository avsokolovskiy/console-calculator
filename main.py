def print_greetings():
    print('Hi pal! You are in the simple calculator 1.0.')


def print_instruction():
    print('''
    Instruction: 
        1. Just follow the console prompts.
        2. To separate decimal part please use "."
        3. To quit, please enter "Q" and hit enter at any time.
    Happy calculations!
    ''')


def get_operand(number):
    while True:
        operand = input('Please input operand #{}: '.format(number))
        calc_stop(operand)
        try:
            float(operand)
        except:
            print('Not a number. Please enter a valid number')
        else:
            if operand.isdigit():
                return int(operand)
            else:
                return float(operand)


def get_operator():
    while True:
        operator = input('Please enter operator (supported operators +, -, *, /): ')
        calc_stop(operator)
        if operator == '+' or operator == '-' or operator == '*' or operator == '/':
            break
        else:
            print('The operator " {} " is not supported'.format(operator))

    return operator


def calculation(operand_1, operand_2, operator):
    if operator == '+':
        return operand_1 + operand_2
    elif operator == '-':
        return operand_1 - operand_2
    elif operator == '*':
        return operand_1 * operand_2
    elif operator == '/':
        return operand_1 / operand_2


def calc_stop(flag):
    if flag == "Q":
        print("Closing the simple calculator 1.0. See you!!!")
        exit()


# Press the green button in the gutter to run the script.
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
            continue
        else:
            result = round(calculation(operand_1, operand_2, operator), 3)
            print('{} {} {} = {}'.format(operand_1, operator, operand_2, result))
