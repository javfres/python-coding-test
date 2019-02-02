#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
The CSV class allows to work with CSV files
Each CSV object contains:
* A list of column names
* A list of dicts for each row
"""


#######################################
# Imports
#######################################
from utils import is_float_try
from masking import mask_str, mask_numeric


#######################################
# CSV class
#######################################

class CSV:

    # Slots for performance
    __slots__ = ['columns', 'data']

    # Constructor
    def __init__(self, columns, data):
        self.columns = columns
        self.data = data

    # This static method is used to load a csv from a file
    @staticmethod
    def load(fname):

        # Open the file
        with open(fname) as f:

            # Process the first line to get the columns
            line = next(f)
            columns = line.strip().split(',')

            # TODO: Check columns are unique

            # Iterate over the file lines
            data = []
            for line in f:

                # Divide the line into a list
                cells = line.strip().split(',')
                cells = map(CSV.from_str, cells)
                cells = list(cells)

                # Append the new row
                dictionary = dict(zip(columns, cells))
                data.append(dictionary)

            # Return the object
            return CSV(columns, data)

    
    @staticmethod
    def from_str(cell):

        """
        This static method will transform a cell into its 'appropriate' type
        NOTE: I'm supposing: str, int, float and None
        """

        # Trim
        cell = cell.strip()

        if cell.isnumeric():
            return int(cell)
        elif is_float_try(cell):
            return float(cell)
        elif len(cell) == 0:
            return None

        # It was a str after all
        return cell


    # Cell to str (used to ignore the None)
    @staticmethod
    def to_str(val):
        if val is None:
            return ''
        return str(val)


    # Return the csv string for stdout
    def __str__(self):
        
        # 1. Calculate the max width per column
        widths = []
        for col in self.columns:
            lst = self.get_column_as_list(col, True)
            width = max([ len(str(row)) for row in lst])
            widths.append(width)

        # Header
        res = ""
        header = " | ".join( [f"{c:{widths[i]}}" for i,c in enumerate(self.columns) ] ) 
        res += header + '\n'

        # Each row
        for row in self.data:
            line = " | ".join( [f"{CSV.to_str(row[c]):{widths[i]}}" for i,c in enumerate(self.columns) ] ) 
            res += line + '\n'

        return res;


    # Get a column as a list
    def get_column_as_list(self, column, with_header=False):

        # Check the column exists
        assert column in self.columns, "Invalid column"

        # The header is optional
        header = [column] if with_header else []

        # Return the column
        return header + [ d[column] for d in self.data ]


    # Replace a column with the data from a list
    def set_column_from_list(self, column, lst):

        # Check the column exists
        assert column in self.columns, "Invalid column"

        # The column list should have the same number of rows
        assert len(lst) == len(self.data)

        # Replace
        for i,val in enumerate(lst):
            self.data[i][column] = val
        

    # Apply the masking for a str column or columns
    def apply_str_masking(self, column):

        # If the passed attribute is a list, apply the method recursively
        if type(column) is list:
            for c in column:
                self.apply_str_masking(c)
            return

        # Check the type
        assert type(column) is str
        assert column in self.columns, "Invalid column"

        # Apply the mask
        for data in self.data:
            data[column] = mask_str(data[column])
        
    # Apply the number mask
    def apply_num_masking(self, column):

        # Check the column exists
        assert column in self.columns, "Invalid column"

        # With the get/set column method is easier
        lst = self.get_column_as_list(column)
        lst_masked = mask_numeric(lst)
        self.set_column_from_list(column, lst_masked)


    # Save the csv into a file
    def save(self, fname):

        # Open the file for writing
        with open(fname, 'w') as f:

            # Write the header
            header = map(str, self.columns)
            header = ','.join(header)
            f.write(header + '\n')

            # Write the rest of the data
            for data in self.data:
                line = [ data[column] for column in self.columns ]
                line = map(CSV.to_str, line)
                line = ','.join(line)
                f.write(line + '\n')



    # Report for a str column
    def report_str(self, column):

        # Check the column exists
        assert column in self.columns, "Invalid column"

        # Get the length of each cell
        lengths = [len(d[column]) for d in self.data]

        # Print report
        print(f"Report for str column '{column}'")
        print(f"* avg {sum(lengths)/len(lengths)}")
        print(f"* max {max(lengths)}")
        print(f"* min {min(lengths)}")



    # Report for a number column
    def report_num(self, column):

        # Check the column exists
        assert column in self.columns, "Invalid column"

        # Get the value for each cell (ignoring None)
        numbers = [ float(d[column]) for d in self.data if not  d[column] is None ]
        
        # Print report
        print(f"Report for numeric column '{column}'")
        print(f"* avg {sum(numbers)/len(numbers)}")
        print(f"* max {max(numbers)}")
        print(f"* min {min(numbers)}")
