#!/usr/bin/env python

"""Testing the execution of OS commands from Python code."""

from __future__ import print_function

import os
import shlex
import signal
import string
import struct
import subprocess
import time

SIGNALS_TO_NAMES_DICT = dict()


def main():
    """Test the available methods starting from the basic ones."""
    os.system('clear')
    prepare_signal_dict()
    test_os_system()
    test_os_popen()
    test_subprocess_call()
    test_subprocess_popen()


# prepare_signal_dict {{{
def prepare_signal_dict():
    """Prepare signal value to signal names dictionary."""
    for name in dir(signal):
        if (name.startswith('SIG') and '_' not in name):
            SIGNALS_TO_NAMES_DICT[getattr(signal, name)] = name

    if 0 not in SIGNALS_TO_NAMES_DICT:
        SIGNALS_TO_NAMES_DICT[0] = 'No signal'
# }}}


# test_os_system {{{
def test_os_system():
    """Test os.system."""
    print('\nTesting os.system()')
    return_value = os.system('date')
    print_return_value(return_value)

    return_value = os.system('non_existing_command')
    print_return_value(return_value)

    return_value = os.system('find /tmp -type f | grep "oo"')
    print_return_value(return_value)

    print('\n*** Try to issue CTRL-C for the following sleep ***')
    return_value = os.system('sleep 5')
    print_return_value(return_value)


def print_return_value(return_value):
    """Print return value from os.system, os.popen."""
    print('return value = {}'.format(return_value))
    if return_value is None:
        print('(success)')
    else:
        return_value_bytes = get_return_value_bytes(return_value)
        print('got signal (lower byte of return value) = {} [{}]'.format(
            return_value_bytes[0],
            SIGNALS_TO_NAMES_DICT[return_value_bytes[0]]))
        print('exit code (higher byte of return value) = {}'.format(
            return_value_bytes[1]))


def get_return_value_bytes(return_value):
    """Return (lower byte, higher byte) tuple created of return_value."""
    return struct.unpack('<BB', struct.pack('<h', return_value))
# }}}


# test_os_popen {{{
def test_os_popen():
    """Test os.popen."""
    print('\nTesting os.popen()')
    stream = os.popen('sleep 5;date -u')
    print('right after os.popen()')
    time.sleep(4)
    print('right after time.sleep()')
    print(stream.read())
    return_value = stream.close()
    print_return_value(return_value)
    time.sleep(3)

    stream = os.popen('top', 'r', 1)
    for _i in range(90):
        print(stream.readline().rstrip())
    stream.close()
    time.sleep(3)
    os.system('clear')

    stream = os.popen('non_existing_command')
    print('after os.popen()')
    return_value = stream.close()
    print_return_value(return_value)
# }}}


# test_subprocess_call {{{
def test_subprocess_call():
    """Test subprocess.call."""
    print('\nTesting subprocess.call()')
    return_value = subprocess.call(['date', '-u'])

    cmd = 'date -u # this is a comment (does not work with string split)'
    return_value = subprocess.call(cmd.split())

    cmd = 'date -u # this is a comment (works with shlex split'
    return_value = subprocess.call(shlex.split(cmd, True))

    cmd = 'date -u -d @12345'
    return_value = subprocess.call(shlex.split(cmd))
    print(return_value)
    # call split on string object (cmd)
    return_value = subprocess.call(cmd.split())
    print(return_value)
    # call split on string class with string object (cmd) in argument
    return_value = subprocess.call(string.split(cmd))
    print(return_value)

    cmd = 'echo "this is a string containing spaces"'
    print("using shlex.split...")
    return_value = subprocess.call(shlex.split(cmd))
    print(return_value)
    print("using string.split...")
    return_value = subprocess.call(cmd.split())
    print(return_value)

    return_value = subprocess.call(shlex.split('ls -al /tmp/foobar'))
    print(return_value)
# }}}


# test_subprocess_popen {{{
def test_subprocess_popen():
    """Test subprocess.Popen."""
    print('\nTesting subprocess.Popen()')
    process = subprocess.Popen('date', stdout=subprocess.PIPE)
    print_output_and_return_code(process)

    process = subprocess.Popen(['date', '-u'], stdout=subprocess.PIPE)
    print_output_and_return_code(process)

    process = subprocess.Popen('date -u', shell=True, stdout=subprocess.PIPE)
    print_output_and_return_code(process)

    ls_process = subprocess.Popen(shlex.split('ls -al /tmp/foobar'),
                                  stdout=subprocess.PIPE)
    print('return value of ls_process = {}'.format(ls_process.returncode))
    grep_process = subprocess.Popen(shlex.split('grep "oo"'),
                                    stdin=ls_process.stdout,
                                    stdout=subprocess.PIPE)
    print('return value of grep_process = {}'.format(grep_process.returncode))
    print_output_and_return_code(grep_process)

    ls_process = subprocess.Popen(shlex.split('find /tmp -type f'),
                                  stdout=subprocess.PIPE)
    print('return value of ls_process = {}'.format(ls_process.returncode))
    grep_process = subprocess.Popen(shlex.split('grep "oo"'),
                                    stdin=ls_process.stdout,
                                    stdout=subprocess.PIPE)
    print('return value of grep_process = {}'.format(grep_process.returncode))
    print_output_and_return_code(grep_process)


def print_output_and_return_code(process):
    """Print output and return code of given process."""
    print('\noutput = >>>{}<<<'.format(process.stdout.read()))
    print('return code = {}'.format(process.returncode))
# }}}


if __name__ == '__main__':
    main()
