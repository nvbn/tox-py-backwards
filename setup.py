from setuptools import setup

VERSION = '0.1'

setup(name='tox-py-backwards',
      description='tox plugin for py-backwards',
      author='Vladimir Iakovlev',
      author_email='nvbn.rm@gmail.com',
      url='https://github.com/nvbn/tox-py-backwards',
      license="MIT ",
      version=VERSION,
      py_modules=['tox_py_backwards'],
      entry_points={'tox': ['py_backwards = tox_py_backwards']},
      install_requires=['tox>=2.0'])
