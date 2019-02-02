#!/usr/bin/env python3
# -*- coding: utf8 -*-

#######################################
# Imports
#######################################
from utils import is_float_try
from masking import mask_str, mask_numeric


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
        
        widths = []

        for col in self.columns:
            lst = self.get_column_as_list(col, True)
            width = max([ len(str(row)) for row in lst])
            widths.append(width)

        res = ""

        header = " | ".join( [f"{c:{widths[i]}}" for i,c in enumerate(self.columns) ] ) 
        res += header + '\n'

        for row in self.data:
            line = " | ".join( [f"{str(row[c]):{widths[i]}}" for i,c in enumerate(self.columns) ] ) 
            res += line + '\n'

        return res;



    def get_column_as_list(self, column, with_header=False):
        assert column in self.columns, "Invalid column"

        header = []
        if with_header:
            header = [column]

        return header + [ d[column] for d in self.data ]


    def set_column_from_list(self, column, lst):
        assert column in self.columns, "Invalid column"
        assert len(lst) == len(self.data)

        for i,val in enumerate(lst):
            self.data[i][column] = val
        


    def apply_str_masking(self, column):

        if type(column) is list:
            for c in column:
                self.apply_str_masking(c)
            return

        assert type(column) is str
        assert column in self.columns, "Invalid column"

        for data in self.data:
            data[column] = mask_str(data[column])
        
    def apply_num_masking(self, column):

        assert column in self.columns, "Invalid column"

        lst = self.get_column_as_list(column)
        lst_masked = mask_numeric(lst)
        self.set_column_from_list(column, lst_masked)


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



    def report_str(self, column):
        assert column in self.columns, "Invalid column"

        lengths = [len(d[column]) for d in self.data]


        print(f"Report for str column {column}")
        print(f"* avg {sum(lengths)/len(lengths)}")
        print(f"* max {max(lengths)}")
        print(f"* min {min(lengths)}")




    def report_num(self, column):
        assert column in self.columns, "Invalid column"

        numbers = [ float(d[column]) for d in self.data if not  d[column] is None ]
        print(numbers)

        print(f"Report for numeric column {column}")
        print(f"* avg {sum(numbers)/len(numbers)}")
        print(f"* max {max(numbers)}")
        print(f"* min {min(numbers)}")