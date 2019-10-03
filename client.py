#!/usr/bin/env python3

"""client

This file contains a very basic socket client.

It is intentionally kept separate from the rest
of the game files. Run the server.py first before
running this file to test.

This client is by no means stable or secure!
Use at your own risk!"""

# Import built-in libraries.
import sys
import socket
import threading
import queue
import pickle
import logging

# Import supplementary libraries.
import pygame
from pygame.locals import *

# Import local modules.
pass





# Client Connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 1776))

x = s.recv(4096)
print(x.decode())

while True:
    msg = input("> ")
    if msg == 'QUIT':
        s.close()
        break
    f = pickle.dumps(msg)
    s.sendall(f)
    r = s.recv(4096)
    g = pickle.loads(r)
    print(g)
