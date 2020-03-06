#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: binary_toggle_list.py
Description: A simple linked list of binary values that you can toggle to
    simulate an adder, or a flip-fop circuit used in quartz clocks.  Each time
    a node in the list goes from 1 to 0, it automatically toggles the next node
    in the list.  Kinda inspired by this video by Steve Mould:
    <https://youtu.be/_2By2ane2I4>

usage: binary_toggle_list.py [-h] [-n LINKS]

Binary Toggle Chain

optional arguments:
  -h, --help            show this help message and exit
  -n LINKS, --number-of-links LINKS

Author: E. Chris Pedro
Created: 2020-03-06


This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org>
"""

import argparse
import sys

from signal import signal, SIGINT


class ToggleNode(object):
    def __init__(self, value):
        """Initializer.
        """
        self.value = value
        self.next = None

    @property
    def value(self):
        """Getter for value.
        """
        return self._value

    @value.setter
    def value(self, value):
        """Setter for value.
        """
        if value != 0 and value != 1:
            raise Exception('value must be 1 or 0.')
        self._value = value

    @property
    def next(self):
        """Getter for next.
        """
        return self._next

    @next.setter
    def next(self, next):
        """Setter for next.
        """
        if next and not isinstance(next, ToggleNode):
            raise Exception('next must be a ToggleNode.')
        self._next = next

    def __str__(self):
        """String method.  Return values of all items in the list.
        """
        return self.value

    def toggle(self):
        """Toggle value, if 1 goes to 0, toggle next in chain too.
        """
        if self.value == 0:
            self.value = 1
        elif self.value == 1:
            self.value = 0
            if self.next:
                self.next.toggle()


class ToggleChain(object):
    def __init__(self):
        """Initializer.
        """
        self.start = None

    @property
    def start(self):
        """Getter for start.
        """
        return self._start

    @start.setter
    def start(self, start):
        """Setter for start.
        """
        if start and not isinstance(start, ToggleNode):
            raise Exception('start node must be a ToggleNode')
        self._start = start

    def push(self, value):
        """Push node onto the linked list.
        """
        new_link = ToggleNode(value)
        new_link.next = self.start
        self.start = new_link

    def pop(self):
        """Pop node off linked list.
        """
        old_link = self._start
        self.start = old_link.next
        del old_link

    def toggle(self):
        """Toggle first flip-flop in the list.
        """
        if self.start:
            self.start.toggle()

    def __str__(self):
        """String method.  Return values of all items in the list.
        """
        node = self.start
        llist = '[ '
        while node:
            llist += '{:d} '.format(node.value)
            node = node.next
        llist += ']'
        return llist


def number_of_links(value):
    """Check value of command line argument -n/--number-of-links
    """
    n = int(value)
    if n <= 0:
        raise argparse.ArgumentTypeError('Chain must have at least one link.')
    return n


def parse_args(args):
    """Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description='Binary Toggle Chain')
    parser.add_argument('-n', '--number-of-links', dest='links', default='5',
                        type=number_of_links)
    return parser.parse_args(args)


def handler(signal_received, frame):
    """Signal handler.
    """
    sys.exit(0)


def main(args):
    """Main method.
    """
    status = 0

    args = parse_args(args)
    print('Number of links: {}'.format(args.links))
    chain = ToggleChain()
    for i in range(args.links):
        chain.push(0)

    toggles = 0
    while True:
        try:
            print(chain)
            print('Number of toggles: {:d} '.format(toggles))
            input('Press Enter to continue ')
            toggles += 1
            chain.toggle()
            print('------------------------------------------------')
        except EOFError:
            return status

    return status


if __name__ == '__main__':
    signal(SIGINT, handler)
    sys.exit(main(sys.argv[1:]))

