#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: fib.py
Description: Classic Comp Sci exercise to write a program to calculate the nth
    value in the Fibonacci sequence.

Author: E. Chris Pedro
Created: 2024-10-01
"""

import argparse
import sys

from signal import signal, SIGINT


def fibonacci(n, values={}):
    if n in values:
        return values[n]
    if n == 0 or n == 1:
        return 1
    values[n] = fibonacci(n - 1, values) + fibonacci(n - 2, values)
    return values[n]


def valid_n(value):
    n = int(value)
    if n < 0:
        raise argparse.ArgumentTypeError('N cannot be negative')
    return n


def parse_args(args):
    parser = argparse.ArgumentParser(description='Fibonacci Calculator')
    parser.add_argument('-n', '--number', dest='n', default='5', type=valid_n)
    return parser.parse_args(args)


def handler(signal_received, frame):
    sys.exit(0)


def main(args):
    args = parse_args(args)
    print(f'{fibonacci(args.n)}')


if __name__ == '__main__':
    signal(SIGINT, handler)
    sys.exit(main(sys.argv[1:]))
