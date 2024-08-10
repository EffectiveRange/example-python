# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/EffectiveRange/example-python/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                            |    Stmts |     Miss |   Branch |   BrPart |   Cover |   Missing |
|-------------------------------- | -------: | -------: | -------: | -------: | ------: | --------: |
| example/\_\_init\_\_.py         |        3 |        0 |        0 |        0 |    100% |           |
| example/example.py              |       35 |        0 |        6 |        0 |    100% |           |
| example/tablePrinter.py         |       30 |        0 |        4 |        0 |    100% |           |
| tests/exampleIntegrationTest.py |       45 |        0 |       10 |        4 |     93% |15->14, 27->32, 45->50, 67->72 |
| tests/exampleTest.py            |       45 |        0 |        2 |        1 |     98% |    13->12 |
| tests/tablePrinterTest.py       |       20 |        0 |        2 |        1 |     95% |    12->11 |
|                       **TOTAL** |  **178** |    **0** |   **24** |    **6** | **97%** |           |

1 empty file skipped.


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/EffectiveRange/example-python/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/EffectiveRange/example-python/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/EffectiveRange/example-python/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/EffectiveRange/example-python/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2FEffectiveRange%2Fexample-python%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/EffectiveRange/example-python/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.