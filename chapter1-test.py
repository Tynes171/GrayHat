'''
Created on Apr 12, 2019

@author: Justin Williams
'''

from ctypes import *

msvcrt = cdll.msvcrt
message_string = "Hows it going?\n"
msvcrt.printf("Trying: %s", message_string)

