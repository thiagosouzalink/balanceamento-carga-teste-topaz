"""
Module for testing.
"""
import unittest

import load_balancing


class TestLoadBalancing(unittest.TestCase):
    """
    Class for performing unit testing with the framework unittest
    """
    def setUp(self):
        """ initial settings """
        valid_file = 'test_txt_files/valid_input.txt'
        invalid_file = 'test_txt_files/invalid_input.txt'
        self.val_content = load_balancing.read_file(valid_file)
        self.inv_content = load_balancing.read_file(invalid_file)

    def test_read_invalid_file(self):
        """ Invalid file read test. """
        _file = 'files/input_error.txt'
        value_return = load_balancing.read_file(_file)
        self.assertIsNone(value_return)

    def test_read_valid_file(self):
        """ Valid file read test. """
        _file = 'files/input.txt'
        value_return = load_balancing.read_file(_file)
        self.assertIsNotNone(value_return)

    def test_get_valid_args(self):
        """ File read test with valid arguments. """
        cond, _ = load_balancing.check_initial_conditions(self.val_content)
        self.assertEqual(cond, '')

    def test_get_invalid_args(self):
        """ File read test with invalid arguments. """
        cond, _ = load_balancing.check_initial_conditions(self.inv_content)
        self.assertNotEqual(cond, '')

    def test_valid_ttask(self):
        """ Valid ttask value test. """
        cond, var = load_balancing.check_initial_conditions(self.val_content)
        ttask = var[0]
        ttask_file = int(self.val_content[0])
        self.assertEqual(cond, '')
        self.assertEqual(ttask, ttask_file)

    def test_invalid_ttask(self):
        """ Invalid ttask value test. """
        cond, var = load_balancing.check_initial_conditions(self.inv_content)
        msg = 'ERRO: Argumento(s) ttask ou/e umax inválido(s)'
        ttask = var[0]
        _range = range(1, 11)
        self.assertEqual(cond, msg)
        self.assertNotIn(ttask, _range)

    def test_valid_umax(self):
        """ Valid umax value test. """
        cond, var = load_balancing.check_initial_conditions(self.val_content)
        umax = var[1]
        umax_file = int(self.val_content[1])
        self.assertEqual(cond, '')
        self.assertEqual(umax, umax_file)

    def test_invalid_umax(self):
        """ Invalid ttask value test. """
        cond, var = load_balancing.check_initial_conditions(self.inv_content)
        msg = 'ERRO: Argumento(s) ttask ou/e umax inválido(s)'
        umax = var[1]
        _range = range(1, 11)
        self.assertEqual(cond, msg)
        self.assertNotIn(umax, _range)

    def test_load_balancing_run_successfully(self):
        """ Test execution of load balancing program successfully. """
        input_test = 'test_txt_files/input_test.txt'
        _file = 'test_txt_files/output_test.txt'
        cost = 4
        expected_output_values = ['1', '1', '1', '1', '0', str(cost)]
        result = load_balancing.run_load_balancing(input_test, _file)
        msg_success = "Execução finalizada com sucesso."
        read_values = [v.strip() for v in load_balancing.read_file(_file)]
        self.assertEqual(read_values, expected_output_values)
        self.assertEqual(result, msg_success)

    def test_load_balancing_input_empty_file(self):
        """ Load balancing program execution test with empty file input. """
        file_test = 'test_txt_files/empty_file.txt'
        _file = 'test_txt_files/output_test.txt'
        result = load_balancing.run_load_balancing(file_test, _file)
        msg_error = 'Erro: Arquivo está vazio.'
        self.assertEqual(result, msg_error)

    def test_load_balancing_input_non_existent_file(self):
        """ Test execution of load balancing program with non-existent
            file input.
        """
        file_test = 'test_txt_files/non_existent_file.txt'
        _file = 'test_txt_files/output_test.txt'
        result = load_balancing.run_load_balancing(file_test, _file)
        msg_error = 'ERRO: Arquivo não existe.'
        self.assertEqual(result, msg_error)


if __name__ == '__main__':
    unittest.main()
