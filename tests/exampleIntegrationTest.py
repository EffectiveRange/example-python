import io
import unittest
from contextlib import redirect_stdout
from unittest import TestCase
from unittest.mock import MagicMock

from context_logger import setup_logging

from example import INetifacesWrapper, Example, TablePrinter


class ExampleTest(TestCase):

    @classmethod
    def setUpClass(cls):
        setup_logging('example-python', 'DEBUG', warn_on_overwrite=False)

    def setUp(self):
        print()

    def test_when_called_with_interface_name(self):
        # Given
        netifaces_wrapper, table_printer = create_components()
        example = Example(netifaces_wrapper, table_printer)

        # When
        with redirect_stdout(io.StringIO()) as output:
            example.example_method('eth0')
            result = output.getvalue()

        # Then
        expected = ('#=================================================#\n'
                    '# interface | mac address       | ip address      #\n'
                    '#-------------------------------------------------#\n'
                    '# eth0      | 00:15:5d:01:c5:60 | 172.27.53.191   #\n'
                    '#=================================================#\n')
        self.assertEqual(expected, result)

    def test_when_called_without_interface_name(self):
        # Given
        netifaces_wrapper, table_printer = create_components()
        example = Example(netifaces_wrapper, table_printer)

        # When
        with redirect_stdout(io.StringIO()) as output:
            example.example_method()
            result = output.getvalue()

        # Then
        expected = ('#=================================================#\n'
                    '# interface | mac address       | ip address      #\n'
                    '#-------------------------------------------------#\n'
                    '# lo        | 00:00:00:00:00:00 | 127.0.0.1       #\n'
                    '# eth0      | 00:15:5d:01:c5:60 | 172.27.53.191   #\n'
                    '# eth1      | 00:15:5D:30:01:00 |                 #\n'
                    '# docker0   | 02:42:b1:d7:00:14 | 172.17.0.1      #\n'
                    '#=================================================#\n')
        self.assertEqual(expected, result)

    def test_when_called_with_interface_name_and_interface_not_found(self):
        # Given
        netifaces_wrapper, table_printer = create_components()
        netifaces_wrapper.get_interface.side_effect = [None]
        example = Example(netifaces_wrapper, table_printer)

        # When
        with redirect_stdout(io.StringIO()) as output:
            example.example_method('wlan0')
            result = output.getvalue()

        # Then
        expected = ('#=================================================#\n'
                    '# interface | mac address       | ip address      #\n'
                    '#-------------------------------------------------#\n'
                    '# wlan0     |                   |                 #\n'
                    '#=================================================#\n')
        self.assertEqual(expected, result)


def create_components():
    interfaces = {
        'lo': {17: [{'addr': '00:00:00:00:00:00'}], 2: [{'addr': '127.0.0.1'}]},
        'eth0': {17: [{'addr': '00:15:5d:01:c5:60'}], 2: [{'addr': '172.27.53.191'}]},
        'eth1': {17: [{'addr': '00:15:5D:30:01:00'}]},
        'docker0': {17: [{'addr': '02:42:b1:d7:00:14'}], 2: [{'addr': '172.17.0.1'}]}
    }
    netifaces_wrapper = MagicMock(spec=INetifacesWrapper)
    netifaces_wrapper.get_interface_names.return_value = interfaces.keys()
    netifaces_wrapper.get_interface.side_effect = lambda name: interfaces.get(name)
    table_printer = TablePrinter([('interface', 9), ('mac address', 17), ('ip address', 15)])
    return netifaces_wrapper, table_printer


if __name__ == '__main__':
    unittest.main()
