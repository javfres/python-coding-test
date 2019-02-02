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
from csv import CSV


#######################################
# Check the python version
#######################################

my_py_version = (3,6)
# The f-str already givesa hint this is for py3
msg = f"This script was intented for Python {my_py_version}"
assert sys.version_info >= my_py_version, msg
        



#######################################
# Main
#######################################

if __name__ == '__main__':
    print(__doc__)


    # Read the CSV
    doc = CSV.load("clientes.csv")
    print(doc)

    # Reports
    doc.report_str('Nombre')
    doc.report_num('Facturado')


    doc.apply_str_masking(['Nombre', 'Email'])
    doc.apply_num_masking('Facturado')

    # "Nombre”, “Email” y “Facturado


    doc.save('clientes_masked.csv')
    print(doc)
