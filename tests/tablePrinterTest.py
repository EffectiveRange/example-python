import unittest
from unittest import TestCase

from context_logger import setup_logging

from example import TablePrinter


class TablePrinterTest(TestCase):

    @classmethod
    def setUpClass(cls):
        setup_logging('example-python', 'DEBUG', warn_on_overwrite=False)

    def setUp(self):
        print()

    def test_print_when_2_columns_created(self):
        # Given
        table_printer = TablePrinter([('column1', 10), ('column2', 12)])

        # When
        result = table_printer.print([['value1', 'value2'], ['value3', 'value4']])

        # Then
        expected = ('#===========================#\n'
                    '# column1    | column2      #\n'
                    '#---------------------------#\n'
                    '# value1     | value2       #\n'
                    '# value3     | value4       #\n'
                    '#===========================#\n')
        self.assertEqual(expected, result)

    def test_print_when_3_columns_created(self):
        # Given
        table_printer = TablePrinter([('column1', 10), ('column2', 12), ('column3', 8)])

        # When
        result = table_printer.print([['value1', 'value2', 'value3'], ['value4', 'value5', 'value6']])

        # Then
        expected = ('#======================================#\n'
                    '# column1    | column2      | column3  #\n'
                    '#--------------------------------------#\n'
                    '# value1     | value2       | value3   #\n'
                    '# value4     | value5       | value6   #\n'
                    '#======================================#\n')
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
