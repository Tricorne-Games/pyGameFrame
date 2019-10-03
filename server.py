#!/usr/bin/env python3

"""server

This file contains a very basic socket server,
useful for making online multiplayer.

It is intentionally kept separate from the rest
of the game files. Run this first before running
the client.py file to test.

This server is by no means stable or secure!
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





# Server Constants
HOST = 'localhost'
PORT = 1776
BUFSIZE = 4096

# Client Thread
class ClientThread(threading.Thread):
    """The ClientThread class, to represent a connection."""
    def __init__(self, conninfo):
        """Initialize a ClientThread."""
        threading.Thread.__init__(self)
        self.conn = conninfo[0]
        self.addr = conninfo[1]
    def run(self):
        """Execute thread operations."""
        print("Connection established!")
        self.conn.sendall(str.encode("Welcome to the server!"))
        while True:
            try:
                data = self.conn.recv(BUFSIZE)
                received = pickle.loads(data)
                if not data:
                    print("Disconnected.")
                    break
                else:
                    print("Received", data)
                    print("Sending", received)
                    newrec = pickle.dumps(received)
                    self.conn.sendall(newrec)
            except:
                print("Lost connection!")
                break
        self.conn.close()

# Prepare Socket Server
Ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Ssocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Do I need this?

# Bind and listen for connections.
try:
    Ssocket.bind((HOST, PORT))
    print("Server started.")
    Ssocket.listen(10)
    print("Listening...")

    while True:
        newconnection = ClientThread(Ssocket.accept())
        newconnection.start()
    Ssocket.close()
        
except socket.error as err:
    print("ERROR", err)

sys.close(0)
