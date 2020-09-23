#!/usr/bin/env python

"""lab0x02.py: implementations of sorting algorithms"""
__author__ = "Jessica Lynch"

from classes.string_list import StringList 
import timeit
from time import perf_counter_ns 

def main():
    try:
        data = StringList()
        data.gen_strings(5, 15, 97, 122)
        print(data.values)
        # data.bubble_sort()
        # data.merge_sort()
        # data.quicksort()
        # data.insertion_sort()
        data.selection_sort()
        print(data.values)
        print(data.is_sorted())
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()