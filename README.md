# Python Playground

A repo I use to play around with Python programming.  Others might find useful.

## binary_toggle_list.py
A simple linked list of binary values that you can toggle to
simulate an adder, or a flip-fop circuit used in quartz clocks.  Each time
a node in the list goes from 1 to 0, it automatically toggles the next node
in the list.  Kinda inspired by this video by Steve Mould.

[![How a quartz watch works - its heart beats 32,768 times a second](http://img.youtube.com/vi/_2By2ane2I4/0.jpg)](https://youtu.be/_2By2ane2I4)

```
usage: binary_toggle_list.py [-h] [-n LINKS]

Binary Toggle Chain

optional arguments:
  -h, --help            show this help message and exit
  -n LINKS, --number-of-links LINKS
```
