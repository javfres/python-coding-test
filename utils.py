#!/usr/bin/env python3
# -*- coding: utf8 -*-


#######################################
# Imports
#######################################
import re

#######################################
# Utils
#######################################

# Check if a str is a float. 
def is_float_try(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def str_mask(cell):
    return re.sub('[a-zA-Z]', 'X', cell)