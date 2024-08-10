#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 Ferenc Nandor Janky <ferenj@effective-range.com>
# SPDX-FileCopyrightText: 2024 Attila Gombos <attila.gombos@effective-range.com>
# SPDX-License-Identifier: MIT

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, Namespace

from context_logger import get_logger, setup_logging

from example import NetifacesWrapper, Example, TablePrinter

log = get_logger('ExampleApp')


def main() -> None:
    arguments = _get_arguments()

    setup_logging('example-python', arguments.log_level, arguments.log_file)

    log.info('Starting example python app', arguments=vars(arguments))

    netifaces_wrapper = NetifacesWrapper()
    table_printer = TablePrinter([('interface', 9), ('mac address', 17), ('ip address', 15)])

    example = Example(netifaces_wrapper, table_printer)

    example.example_method(arguments.interface)


def _get_arguments() -> Namespace:
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f', '--log-file', help='log file path')
    parser.add_argument('-l', '--log-level', help='logging level', default='info')

    parser.add_argument('-i', '--interface', help='network interface name')

    return parser.parse_args()


if __name__ == '__main__':
    main()
