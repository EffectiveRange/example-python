# SPDX-FileCopyrightText: 2024 Ferenc Nandor Janky <ferenj@effective-range.com>
# SPDX-FileCopyrightText: 2024 Attila Gombos <attila.gombos@effective-range.com>
# SPDX-License-Identifier: MIT

from typing import Optional, Any

import netifaces
from context_logger import get_logger

from example import INetifacesWrapper, ITablePrinter

log = get_logger('Example')


class Example(object):

    def __init__(self, netifaces_wrapper: INetifacesWrapper, table_printer: ITablePrinter) -> None:
        self._netifaces_wrapper = netifaces_wrapper
        self._table_printer = table_printer

    def example_method(self, interface_name: Optional[str] = None) -> None:
        interface_names = self._netifaces_wrapper.get_interface_names()

        interface_infos = []

        if interface_name:
            log.info('Retrieving interface info', interface=interface_name)

            interface_infos.append(self._get_interface_info(interface_name))
        else:
            log.info('Retrieving info for all interfaces')

            for name in interface_names:
                interface_infos.append(self._get_interface_info(name))

        self._table_printer.print(interface_infos)

    def _get_interface_info(self, interface_name: str) -> list[str]:
        interface = self._get_interface(interface_name)

        if not interface:
            return [interface_name, '', '']

        mac_address = self._get_address(interface, netifaces.AF_LINK)
        ip_address = self._get_address(interface, netifaces.AF_INET)

        return [interface_name, mac_address, ip_address]

    def _get_interface(self, interface_name: str) -> Optional[dict[int, list[Any]]]:
        try:
            return self._netifaces_wrapper.get_interface(interface_name)
        except ValueError as error:
            log.error('Error retrieving interface', interface=interface_name, error=str(error))
            return None

    def _get_address(self, interface: dict[int, list[Any]], address_family: int) -> str:
        address = interface.get(address_family)

        return str(address[0].get('addr', '')) if address else ''
