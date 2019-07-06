#!/usr/bin/env python3
"""
serve.py

Instantiates a socket-adventure `Server` and serves it on a specified
port.

You should not need to make any changes in this file.
"""


import sys
from server import Server


def main():
    """ Ah, I see you're a man of cultre as well. """
    try:
        port = int(sys.argv[1])
    except IndexError:
        print("Please include a port number, eg: python serve.py 50000")
        exit(-1)

    server = Server(port)
    server.serve()


if __name__ == "__main__":
    main()
