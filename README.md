# example-python
Example showcasing the dev tooling for Python based development

## Installation

### Install from source root directory

```bash
pip install .
```

### Install from source distribution

1. Create source distribution
    ```bash
    python setup.py sdist
    ```

2. Install from distribution file
    ```bash
    pip install dist/example-python-*.tar.gz
    ```

3. Install from GitHub repository
    ```bash
    pip install git+https://github.com/EffectiveRange/example-python.git@latest
    ```

## Usage

### Options

```commandline
$ bin/example-python.py --help
usage: example-python.py [-h] [-f LOG_FILE] [-l LOG_LEVEL] [-i INTERFACE]

optional arguments:
-h, --help            show this help message and exit
-f LOG_FILE, --log-file LOG_FILE
log file path (default: None)
-l LOG_LEVEL, --log-level LOG_LEVEL
logging level (default: info)
-i INTERFACE, --interface INTERFACE
network interface name (default: None)
```

### Running the application

```commandline
$ bin/example-python.py
2024-06-19T05:27:47.761649Z [info     ] Starting example python app    [ExampleApp] app_version=0.1.0 application=example-python arguments={'log_file': None, 'log_level': 'info', 'interface': None} hostname=Legion7iPro
2024-06-19T05:27:47.776165Z [info     ] Retrieving info for all interfaces [Example] app_version=0.1.0 application=example-python hostname=Legion7iPro
#=================================================#
# interface | mac address       | ip address      #
#-------------------------------------------------#
# lo        | 00:00:00:00:00:00 | 127.0.0.1       #
# eth0      | 00:15:5d:01:c5:60 | 172.27.53.191   #
# docker0   | 02:42:b1:d7:00:14 | 172.17.0.1      #
#=================================================#
```

```commandline
$ bin/example-python.py -i eth0
2024-06-19T05:33:40.646111Z [info     ] Starting example python app    [ExampleApp] app_version=0.1.0 application=example-python arguments={'log_file': None, 'log_level': 'info', 'interface': 'eth0'} hostname=Legion7iPro
2024-06-19T05:33:40.668390Z [info     ] Retrieving interface info      [Example] app_version=0.1.0 application=example-python hostname=Legion7iPro interface=eth0
#=================================================#
# interface | mac address       | ip address      #
#-------------------------------------------------#
# eth0      | 00:15:5d:01:c5:60 | 172.27.53.191   #
#=================================================#
```

```commandline
$ bin/example-python.py -i eth1 -l error
2024-06-19T05:34:17.685515Z [error    ] Error retrieving interface     [Example] app_version=0.1.0 application=example-python error=You must specify a valid interface name. hostname=Legion7iPro interface=eth1
#=================================================#
# interface | mac address       | ip address      #
#-------------------------------------------------#
# eth1      |                   |                 #
#=================================================#
```