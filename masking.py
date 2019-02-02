#!/usr/bin/env python3
# -*- coding: utf8 -*-


#######################################
# Imports
#######################################
import re



#######################################
# Mask str function
#######################################
def mask_str(cell):

    assert type(cell) is str, "Invalid type"

    return re.sub('[a-zA-Z]', 'X', cell)



#######################################
# Mask numeric column
#######################################
def mask_numeric(column):

    assert type(column) is list, "Invalid type"

    numbers = [ cell for cell in column if not cell is None ]
    average = sum( numbers ) / len(numbers)

    result = []

    for val in column:
        if val is None:
            result.append(None)
        else:
            result.append(average)

    return result