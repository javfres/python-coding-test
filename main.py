#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
Data masking test
Author: Javier
"""


#######################################
# Check the python version
#######################################
import sys
my_py_version = (3,6)
# The f-str already gives a hint this is for py3
msg = f"This script was intended for Python {my_py_version}"
assert sys.version_info >= my_py_version, msg
        

#######################################
# Imports
#######################################

# Import the CSV class to process the CSV
from utils import title
from csv import CSV



#######################################
# Main
#######################################

if __name__ == '__main__':

    # Print the file's doc
    print(__doc__)

    # Read the CSV
    doc = CSV.load("clientes.csv")

    title("Reading the CSV")
    print(doc)

    # Reports
    title("Showing the reports")
    
    # Reports are printed to std, they should be returned for further processing
    # but for this test I believe it's good enough
    doc.report_str('Nombre')
    doc.report_num('Facturado')

    # Masking
    # the CSV uses the functions defined in masking.py
    title("Masking sensible data")
    doc.apply_str_masking(['Nombre', 'Email'])
    doc.apply_num_masking('Facturado')

    # Save the result
    title("Saving the result")
    doc.save('clientes_masked.csv')
    print(doc)
