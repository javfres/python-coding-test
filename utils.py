#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
Some extra utils
"""


#######################################
# Imports
#######################################
import re

#######################################
# Check if a str is a float 
#######################################

# I took it from SO. Is there a str.isfloat() ???
def is_float_try(str):
    try:
        float(str)
        return True
    except ValueError:
        return False



#######################################
# Title func
#######################################

def title(msg, length=60, ch='='):
    
    "A function that prints a title"

    print(ch * length)
    print(f"{ch}{msg:^{length-2}}{ch}")
    print(ch * length)