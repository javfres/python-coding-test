#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
Data masking test
Author: Javier
"""

#######################################
# Imports
#######################################
import sys


#######################################
# Check the python version
#######################################

my_py_version = (3,6)
# The f-str already givesa hint this is for py3
msg = f"This script was intented for Python {my_py_version}"
assert sys.version_info >= my_py_version, msg
        
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





#######################################
# CSV class
#######################################

class CSV:

    __slots__ = ['columns', 'data']

    # 
    def __init__(self, columns, data):

        self.columns = columns
        self.data = data


    @staticmethod
    def load(fname):

        with open(fname) as f:

            # Process the first line to get the columns
            line = next(f)
            columns = line.strip().split(',')

            data = []

            for line in f:
                cells = line.strip().split(',')
                cells = map(CSV.from_str, cells)
                cells = list(cells)

                dictionary = dict(zip(columns, cells))
                data.append(dictionary)

            return CSV(columns, data)

    
    @staticmethod
    def from_str(cell):

        # NOTE: I'm suppossing: str, int, float and None
        "This static method will transform a cell into its 'appropriate' type"

        cell = cell.strip()


        if cell.isnumeric():
            return int(cell)
        elif is_float_try(cell):
            return float(cell)
        elif len(cell) == 0:
            return None

        return cell


    @staticmethod
    def to_str(val):

        if val is None:
            return ''
        return str(val)



    def __str__(self):
        return ""


    def apply_masking(self, column):

        pass

    def save(self, fname):

        with open(fname, 'w') as f:

            # Write the header
            header = map(str, self.columns)
            header = ','.join(header)
            f.write(header + '\n')

            for data in self.data:

                line = [ data[column] for column in self.columns ]
                line = map(CSV.to_str, line)
                line = ','.join(line)
                f.write(line + '\n')


#######################################
# Main
#######################################

if __name__ == '__main__':
    print(__doc__)


    # Read the CSV
    doc = CSV.load("clientes.csv")
    print(doc)


    # "Nombre”, “Email” y “Facturado


    doc.save('clientes_masked.csv')