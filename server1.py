#!/usr/bin/env python3

import socket

s = socket.socket()
s.bind(("", 37712))
s.listen()
client = s.accept()
