# SPDX-FileCopyrightText: 2024 Ferenc Nandor Janky <ferenj@effective-range.com>
# SPDX-FileCopyrightText: 2024 Attila Gombos <attila.gombos@effective-range.com>
# SPDX-License-Identifier: MIT

class ITablePrinter(object):

    def print(self, rows: list[list[str]]) -> str:
        raise NotImplementedError()


class TablePrinter(ITablePrinter):

    def __init__(self, columns: list[tuple[str, int]]) -> None:
        self._column_names = [column[0] for column in columns]
        self._column_widths = [column[1] for column in columns]
        self._width = sum(self._column_widths) + len(self._column_widths) * 3 - 1

    def print(self, rows: list[list[str]]) -> str:
        output = self._print_header()

        for row in rows:
            output += self._print_row(row)

        output += self._print_separator('=')

        return output

    def _print_header(self) -> str:
        output = self._print_separator('=')
        output += self._print_row(self._column_names)
        output += self._print_separator('-')

        return output

    def _print_row(self, row: list[str]) -> str:
        columns = []

        for i, width in enumerate(self._column_widths):
            columns.append(row[i].ljust(width))

        line = ' | '.join(columns)

        return self._print_line(f' {line} ')

    def _print_separator(self, symbol: str) -> str:
        return self._print_line(self._width * symbol)

    def _print_line(self, line: str) -> str:
        output = f'#{line}#'

        print(output)

        return f'{output}\n'
