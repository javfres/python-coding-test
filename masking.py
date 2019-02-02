#!/usr/bin/env python3
# -*- coding: utf8 -*-


#######################################
# Imports
#######################################
import re



#######################################
# Mask str function
#######################################

def mask_str(cell: str):

    "Processes a sensible data str removing all alpha characters"

    # Check the input type
    assert type(cell) is str, "Invalid type"

    # TODO: I'm not taking into account other utf chars (tildes, etc.)
    return re.sub('[a-zA-Z]', 'X', cell)



#######################################
# Mask numeric column
#######################################

def mask_numeric(column: list):

    """
    Processes a list of cells with sensible numbers replacing each number
    with the average of all found numbers. It keep the None values.
    """

    # Check the input type
    assert type(column) is list, "Invalid type"

    # Retrieve the numbers (discard the None elements in the list)
    numbers = [ cell for cell in column if not cell is None ]
    # Calculate the average
    average = sum(numbers) / len(numbers)

    # Return the list
    return [ None if val is None else average for val in column ]

