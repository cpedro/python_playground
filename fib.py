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


def fibonacci_recur(n, values={}):
    if n in values:
        return values[n]
    if n == 0:
        return 0
    if n == 1:
        return 1

    values[n] = fibonacci_recur(n - 1, values) + fibonacci_recur(n - 2, values)
    return values[n]


def fibonacci_iter(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


def valid_n(value):
    n = int(value)
    if n < 0:
        raise argparse.ArgumentTypeError('N cannot be negative')
    return n


function_handler = {
    'recursive': lambda data: fibonacci_recur(data),
    'iterative': lambda data: fibonacci_iter(data)
}


def parse_args(args):
    parser = argparse.ArgumentParser(description='Fibonacci Calculator')
    parser.add_argument('-n', '--number', dest='n', default='5', type=valid_n)
    parser.add_argument('-f', '--function', default='iterative',
                        choices=list(function_handler.keys()),
                        help='Function to use to calculate')
    return parser.parse_args(args)


def handler(signal_received, frame):
    sys.exit(0)


def main(args):
    args = parse_args(args)
    if args.function in function_handler:
        print(function_handler[args.function](args.n))
    else:
        raise argparse.ArgumentTypeError('Unsupported function')


if __name__ == '__main__':
    signal(SIGINT, handler)
    sys.exit(main(sys.argv[1:]))
