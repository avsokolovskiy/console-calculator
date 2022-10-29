"""Simple calculator unit tests"""
import unittest
from unittest.mock import patch
import io
from contextlib import redirect_stdout
import calc_main

MSG_GREETINGS = 'Hi pal! You are in the simple calculator 1.0.'
MSG_INSTRUCTION = '''Instruction:
        1. Just follow the console prompts.
        2. To separate decimal part please use "."
        3. To quit, please enter "Q" and hit enter at any time.
    Happy calculations!'''
QUIT_ARG = 'Q'
VALID_OPRND_ARG = '32'
VALID_OPRTR_ARG = '+'
NOT_VALID_OPRND_ARG = 'AaaA'
NOT_VALID_OPRTR_ARG = 'BBBB'
test_data_add = [[1, 2, 3], [-1, -2, -3], [-1, 2, 1], [1, 2.5, 3.5]]
test_data_sub = [[1, 2, -1], [-1, -2, 1], [-1, 2, -3], [1, 2.5, -1.5]]
test_data_mult = [[2, 3, 6], [-2, -2, 4], [-2, 6, -12], [2.5, 2.5, 6.25]]
test_data_dev = [[4, 2, 2], [5, 2, 2.5], [-10, -2, 5], [8, -2, -4], [0, 5, 0], [8, 3.2, 2.5]]


class SimpleCalcTests(unittest.TestCase):
    """Test cases for simple calculator."""

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        print(f'The {self.id()} case is executed')

    def tearDown(self) -> None:
        print(f'The {self.id()} case is closed')

    def test_greetings(self) -> None:
        """User greetings print test function"""
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            calc_main.print_greetings()
        test_obj = str(captured_output.getvalue()).strip()
        self.assertEqual(MSG_GREETINGS, test_obj)

    def test_instructions(self) -> None:
        """User manual print test function"""
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            calc_main.print_instruction()
        test_obj = str(captured_output.getvalue()).strip()
        self.assertEqual(MSG_INSTRUCTION, test_obj)

    def test_stop(self) -> None:
        """User exit by input Q test function"""
        with self.assertRaises(SystemExit) as context_manager:
            calc_main.calc_stop(QUIT_ARG)
        self.assertEqual(None, context_manager.exception.code)

    @patch('builtins.input', lambda *args: QUIT_ARG)
    def test_stop_from_get_operand(self) -> None:
        """User exit by input Q test function in operand input"""
        with self.assertRaises(SystemExit) as context_manager:
            calc_main.get_operand('1')
        self.assertEqual(None, context_manager.exception.code)

    @patch('builtins.input', lambda *args: QUIT_ARG)
    def test_stop_from_get_operator(self) -> None:
        """User exit by input Q test function in operator input"""
        with self.assertRaises(SystemExit) as context_manager:
            calc_main.get_operator()
        self.assertEqual(None, context_manager.exception.code)

    @patch('builtins.input', lambda *args: VALID_OPRND_ARG)
    def test_get_operand(self) -> None:
        """Tests for valid user input"""
        test_oprnd = calc_main.get_operand('1')
        self.assertEqual(VALID_OPRND_ARG, str(test_oprnd))

    @patch('builtins.input', lambda *args: VALID_OPRTR_ARG)
    def test_get_operator(self) -> None:
        """Tests for valid user input"""
        test_obj = calc_main.get_operator()
        self.assertEqual(VALID_OPRTR_ARG, test_obj)

    # NEED HELP!!!
    @patch('builtins.input', lambda *args: VALID_OPRND_ARG)
    def test_get_operand_not_valid_input(self) -> None:
        """Tests for not valid user input"""
        # with self.assertRaises(ValueError) as context_manager:
        #    calc_main.get_operand(1)
        # self.assertEqual(ValueError, calc_main.get_operand, '1')
        # pass

    @patch('builtins.input', lambda *args: NOT_VALID_OPRTR_ARG)
    def test_get_operator_not_valid_input(self) -> None:
        """Tests for not valid user input"""
        # test_obj = calc_main.get_operator()
        # self.assertNotEqual(NOT_VALID_OPRTR_ARG, test_obj)
        # pass

    ##############

    def test_addition(self) -> None:
        """Tests for addition"""
        self.calc_verification(test_data=test_data_add, test_operator='+')

    def test_subtraction(self) -> None:
        """Tests for subtraction"""
        self.calc_verification(test_data=test_data_sub, test_operator='-')

    def test_multiplication(self) -> None:
        """Tests for multiplication"""
        self.calc_verification(test_data=test_data_mult, test_operator='*')

    def test_division(self) -> None:
        """Tests for division"""
        self.calc_verification(test_data=test_data_dev, test_operator='/')

    def test_devision_by_0_raises_exeption(self) -> None:
        """Tests for division by zero"""
        self.assertRaises(Exception, calc_main.calculation, '5', '0', '/')

    def calc_verification(self, test_data, test_operator) -> None:
        """Method for verification execution"""
        for dt_case in test_data:
            test_obj = calc_main.calculation(
                operand_a=dt_case[0], operand_b=dt_case[1], akt_operator=test_operator
            )
            print(f'{dt_case[0]}{test_operator}{dt_case[1]}={test_obj}, expected => {dt_case[2]}')
            self.assertEqual(dt_case[2], test_obj)


if __name__ == '__main__':
    unittest.main()
