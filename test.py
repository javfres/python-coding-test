#!/usr/bin/env python3
# -*- coding: utf8 -*-


#######################################
# Imports
#######################################
from utils import is_float_try, str_mask
import unittest



class TESTCSV(unittest.TestCase):

    def test_str_mask(self):
        self.assertEqual(str_mask('javi@secret.com'), 'XXXX@XXXXXX.XXX')




if __name__ == '__main__':
    unittest.main()