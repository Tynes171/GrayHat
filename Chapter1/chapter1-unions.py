from ctypes import *

class coors_light(Union):
    _fields_ = [
        ("coors_long", c_long),
        ("coors_int", c_int),
        ("coors_char", c_char * 8),
        ]
    

value = raw_input("Enter the amount of coors light to into the beer vat: ")
my_coors = coors_light(int(value))
print "Coors amount as a long %ld" %my_coors.coors_long
print "Coors amount as an int %d" %my_coors.coors_int
print "Coors amount as a character %s" %my_coors.coors_char

