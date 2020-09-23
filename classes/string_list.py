#!/usr/bin/env python

"""string_list.py: a class for generating lists of strings"""
__author__ = "Jessica Lynch"

import random
from time import perf_counter_ns
import classes.sorts as sorts

class StringList:

    # CONSTRUCTOR
    #---------------------------------------------
    def __init__(self, N, k, min_v, max_v):
        """A list of strings with sorting methods        
        
        Parameters:
        arg1 (int): number of elements
        arg2 (int): string length
        arg3 (int): minimum ascii value
        arg4 (int): maxiumum ascii value

        Attributes:
        values: string list
        """
        self.values = []
        self.N = N
        self.k = k
        self.min_v = min_v
        self.max_v = max_v
        self.generate_test_list(N, k, min_v, max_v)
            
    # METHODS
    #---------------------------------------------
    def generate_test_list(self, N, k, min_v, max_v):
        """Generate a list of strings"""
        if min_v < 1 or max_v > 256:
            raise ValueError("generate_test_list failed: min/max out of ASCII range")
        self.min_v = min_v
        self.max_v = max_v
        self.values = [''.join(chr(random.randint(min_v, max_v)) for _ in range(k)) for _ in range(N)]

    def bubble_sort(self):
        """An elementary sorting algorithm"""
        self.values = sorts.bubble_sort(self.values)

    def counting_sort(self, debug=False):
        """A comparison-free sorting algorithm"""
        self.values = sorts.counting_sort(self.values, debug)

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

    def radix_sort(self, debug=False):
        """A comparison-free sorting algorithm"""
        self.values = sorts.radix_sort(self.values, debug)

    def selection_sort(self, debug=False):
        """An elementary sorting algorithm"""
        self.values = sorts.selection_sort(self.values, debug)

    def is_sorted(self):
        L = self.values
        for i in range(len(L) - 1):
            if L[i+1] < L[i]:
                return False
        return True

    def verify_sorts(self):
        """Verify that all sorts are working correctly"""
        N = self.N
        k = self.k
        min_v = self.min_v
        max_v = self.max_v
        # Add all sorting functions to a list
        sorting_functions = [self.bubble_sort, self.counting_sort, self.insertion_sort, self.radix_sort, self.selection_sort, self.merge_sort, self.quicksort]

        # Generate a list of strings for each sorting function
        # and test if the function sorts correctly
        for sf in sorting_functions:
            print(f"Generating list of length {N}, key width of {k}")
            self.generate_test_list(N, k, min_v, max_v)
            print(f"Sorting with {(sf.__name__).upper().replace('_', ' ')}")
            sf()
            print("Verifying...", "Sorted!" if self.is_sorted() else "Failed!", end="\n\n")

    def print(self):
        print(self.values)