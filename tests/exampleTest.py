import unittest
from unittest import TestCase
from unittest.mock import MagicMock

from context_logger import setup_logging

from example import ITablePrinter, INetifacesWrapper, Example


class ExampleTest(TestCase):

    @classmethod
    def setUpClass(cls):
        setup_logging('example-python', 'DEBUG', warn_on_overwrite=False)

    def setUp(self):
        print()

    def test_when_called_with_interface_name(self):
        # Given
        netifaces_wrapper, table_printer = create_mocks()
        example = Example(netifaces_wrapper, table_printer)

        # When
        example.example_method('int1')

        # Then
        table_printer.print.assert_called_once_with([['int1', 'mac_address1', 'ip_address1']])

    def test_when_called_without_interface_name(self):
        # Given
        netifaces_wrapper, table_printer = create_mocks()
        example = Example(netifaces_wrapper, table_printer)

        # When
        example.example_method()

        # Then
        table_printer.print.assert_called_once_with([
            ['int1', 'mac_address1', 'ip_address1'], ['int2', 'mac_address2', 'ip_address2']
        ])

    def test_when_called_with_interface_name_and_interface_not_found(self):
        # Given
        netifaces_wrapper, table_printer = create_mocks()
        netifaces_wrapper.get_interface.side_effect = ValueError('Invalid interface name')
        example = Example(netifaces_wrapper, table_printer)

        # When
        example.example_method('int1')

        # Then
        table_printer.print.assert_called_once_with([['int1', '', '']])

    def test_when_called_with_interface_name_and_mac_address_not_found(self):
        # Given
        netifaces_wrapper, table_printer = create_mocks()
        netifaces_wrapper.get_interface.side_effect = [{2: [{'addr': 'ip_address1'}]}]
        example = Example(netifaces_wrapper, table_printer)

        # When
        example.example_method('int1')

        # Then
        table_printer.print.assert_called_once_with([['int1', '', 'ip_address1']])

    def test_when_called_with_interface_name_and_ip_address_not_found(self):
        # Given
        netifaces_wrapper, table_printer = create_mocks()
        netifaces_wrapper.get_interface.side_effect = [{17: [{'addr': 'mac_address1'}]}]
        example = Example(netifaces_wrapper, table_printer)

        # When
        example.example_method('int1')

        # Then
        table_printer.print.assert_called_once_with([['int1', 'mac_address1', '']])


def create_mocks():
    netifaces_wrapper = MagicMock(spec=INetifacesWrapper)
    netifaces_wrapper.get_interface_names.return_value = ['int1', 'int2']
    netifaces_wrapper.get_interface.side_effect = [
        {17: [{'addr': 'mac_address1'}], 2: [{'addr': 'ip_address1'}]},
        {17: [{'addr': 'mac_address2'}], 2: [{'addr': 'ip_address2'}]}
    ]
    table_printer = MagicMock(spec=ITablePrinter)
    return netifaces_wrapper, table_printer


if __name__ == '__main__':
    unittest.main()
