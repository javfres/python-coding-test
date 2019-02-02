#!/usr/bin/env python3
# -*- coding: utf8 -*-


#######################################
# Imports
#######################################
from masking import mask_str, mask_numeric
import unittest



class TESTCSV(unittest.TestCase):

    def test_mask_str(self):
        self.assertEqual(mask_str('javi@secret.com'), 'XXXX@XXXXXX.XXX')


    def test_mask_numeric(self):
        self.assertEqual(mask_numeric([10,5]), [7.5, 7.5])
        self.assertEqual(mask_numeric([1,1,1]), [1,1,1])
        self.assertEqual(mask_numeric([10,5,5,2]), [5.5,5.5,5.5,5.5])


    def test_mask_numeric_gaps(self):
        self.assertEqual(mask_numeric([10,5,None]), [7.5,7.5,None])
        self.assertEqual(mask_numeric([1,None,1,1]), [1,None,1,1])
        self.assertEqual(mask_numeric([10,5,None,5,2]), [5.5,5.5,None,5.5,5.5])



if __name__ == '__main__':
    unittest.main()