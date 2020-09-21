#!/usr/bin/env python

"""integer_list.py: a class for generating integer lists easily"""
__author__ = "Jessica Lynch"

import random
from time import perf_counter_ns
import classes.sorts as sorts
import sys

class IntegerList:

    # CONSTRUCTOR
    #---------------------------------------------
    def __init__(self, file_path=None):
        """A list of integers with sorting methods        
        
        Parameters:
        arg1 (str): initializes with data if filename is provided (optional)

        Attributes:
        values: integer list
        """
        self.values = []
        if file_path != None:
            self.read_ints(file_path)

    # METHODS
    #---------------------------------------------
    def read_ints(self, file_path):        
        with open(file_path, "r") as f:
            self.values = [int(x) for x in f]

    def gen_ints(self, num_ints, min_val=None, max_val=None):
        if min_val is None:
            min_val = sys.maxsize * -1
        if max_val is None:
            max_val = sys.maxsize
        self.values = [random.randint(min_val, max_val) for _ in range(num_ints)]
            
    def bubble_sort(self):
        """A simple sorting algorithm"""
        self.values = sorts.bubble_sort(self.values)

    def merge_sort(self, debug=False):
        """A divide-and-conquer sorting algorithm"""
        self.values = sorts.merge_sort(self.values, debug)

    def quick_sort(self, debug=False):
        """A divide-and-conquer sorting algorithm"""
        last_index = len(self.values) - 1
        self.values = sorts.quicksort(self.values, 0, last_index, debug)

    def is_sorted(self):
        L = self.values
        for i in range(len(L) - 1):
            if L[i+1] < L[i]:
                return False

        return True