#!/usr/bin/env python

"""string_list.py: a class for generating lists of strings"""
__author__ = "Jessica Lynch"

import random
from time import perf_counter_ns
import classes.sorts as sorts

class StringList:

    # CONSTRUCTOR
    #---------------------------------------------
    def __init__(self, file_path=None):
        """A list of strings with sorting methods        
        
        Parameters:
        arg1 (str): initializes with data if filename is provided (optional)

        Attributes:
        values: string list
        """
        self.values = []
        if file_path != None:
            self.read_strings(file_path)

    # METHODS
    #---------------------------------------------
    def read_strings(self, file_path):        
        with open(file_path, "r") as f:
            self.values = [str(x).rstrip() for x in f]

    def gen_strings(self, N, k, min_v, max_v):
        """Generate a list of strings"""
        if min_v < 1 or max_v > 126:
            raise ValueError("Out of ASCII range: use min and max values between 1 and 126")
        self.values = [''.join(chr(random.randint(min_v, max_v)) for _ in range(k)) for _ in range(N)]

    def generate_test_list(self, N, k, min_v, max_v):
        """Generate a list of strings for testing sorting functions"""
        self.gen_strings(N, k, min_v, max_v)

    def bubble_sort(self):
        """An elementary sorting algorithm"""
        self.values = sorts.bubble_sort(self.values)

    def insertion_sort(self, debug=False):
        """An elementary sorting algorithm"""
        self.values = sorts.insertion_sort(self.values, debug)

    def merge_sort(self, debug=False):
        """A divide-and-conquer sorting algorithm"""
        self.values = sorts.merge_sort(self.values, debug)

    def quicksort(self, debug=False):
        """A divide-and-conquer sorting algorithm"""
        last_index = len(self.values) - 1
        self.values = sorts.quicksort(self.values, 0, last_index, debug)

    def selection_sort(self, debug=False):
        """An elementary sorting algorithm"""
        self.values = sorts.selection_sort(self.values, debug)

    def is_sorted(self):
        L = self.values
        for i in range(len(L) - 1):
            if L[i+1] < L[i]:
                return False
        return True

    def verify_sorts(self, N, k, min_v, max_v):
        """Verify that all sorts are working correctly"""
        # Add all sorting functions to a list
        sorting_functions = [self.bubble_sort, self.insertion_sort, self.selection_sort, self.merge_sort, self.quicksort]

        # Generate a list of strings for each sorting function
        # and test if the function sorts correctly
        for sf in sorting_functions:
            print(f"Generating list of length {N}, key width of {k}")
            self.generate_test_list(N, k, min_v, max_v)
            print(f"Sorting with {sf.__name__}")
            sf()
            print("Verifying...", "Sorted!" if self.is_sorted() else "Failed!", end="\n\n")

