# Tox plugin for py-backwards
 
Compiles python code with [py-backwards](https://github.com/nvbn/py-backwards)
before running tests with tox.

## Installation

```bash
pip install tox-py-backwards
```

## Usage

Add `py_backwards = true` to `tox.ini` in `testenv` section, like:

```ini
[tox]
envlist = py27,py33,py34,py35,py36

[testenv]
deps = pytest
commands = py.test
py_backwards = true
```

## License MIT
