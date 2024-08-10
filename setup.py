from setuptools import setup

setup(
    name='example-python',
    version='1.0.0',
    description='Example Python project',
    long_description='Example showcasing the dev tooling for Python based development',
    author='Ferenc Nandor Janky & Attila Gombos',
    author_email='info@effective-range.com',
    packages=['example'],
    scripts=['bin/example-python.py'],
    install_requires=['netifaces',
                      'python-context-logger@git+https://github.com/EffectiveRange/python-context-logger.git@latest']
)
