# SPDX-FileCopyrightText: 2024 Ferenc Nandor Janky <ferenj@effective-range.com>
# SPDX-FileCopyrightText: 2024 Attila Gombos <attila.gombos@effective-range.com>
# SPDX-License-Identifier: MIT

from typing import Any

import netifaces


class INetifacesWrapper(object):

    def get_interface_names(self) -> list[str]:
        raise NotImplementedError

    def get_interface(self, interface_name: str) -> dict[int, list[Any]]:
        raise NotImplementedError


class NetifacesWrapper(INetifacesWrapper):

    def get_interface_names(self) -> list[str]:
        return netifaces.interfaces()  # type: ignore

    def get_interface(self, interface_name: str) -> dict[int, list[Any]]:
        return netifaces.ifaddresses(interface_name)  # type: ignore
