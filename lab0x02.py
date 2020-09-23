#!/usr/bin/env python

"""lab0x02.py: implementations of sorting algorithms"""
__author__ = "Jessica Lynch"

from classes.string_list import StringList 
import timeit
from time import perf_counter_ns 

def main():
    try:
        strings = StringList()
        # strings.generate_test_list(5, 15, 97, 122)
        strings.verify_sorts(5, 15, 97, 122)
        strings2 = StringList("strings.txt")
        print(strings2.values)
        # print(strings.values)
        # strings.bubble_sort()
        # strings.merge_sort()
        # strings.quicksort()
        # strings.insertion_sort()
        strings.selection_sort()
        # print(strings.values)
        # print(strings.is_sorted())
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()