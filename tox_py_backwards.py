from tox import hookimpl


@hookimpl
def tox_addoption(parser):
    parser.add_testenv_attribute(
        name='py_backwards',
        type="bool",
        default=False,
        help='compile code with py-backwards before running tests')


script = '''
VERSION=$(python -c 'import sys; print("{{}}.{{}}".format(*sys.version_info[:2]))')
rm -rf .tox/py_backwards/
mkdir .tox/py_backwards/
cp -a * .tox/py_backwards/
py-backwards -i .tox/py_backwards/ -o .tox/py_backwards/ -t $VERSION
cd .tox/py_backwards/
{}
rm -rf .tox/py_backwards/
'''


@hookimpl
def tox_runtest_pre(venv):
    if venv.envconfig.py_backwards:
        original_command = '\n'.join(' '.join(command)
                                     for command in venv.envconfig.commands)
        venv.envconfig.commands = [['sh', '-c',
                                    script.format(original_command)]]
        venv.envconfig.whitelist_externals.append('sh')
