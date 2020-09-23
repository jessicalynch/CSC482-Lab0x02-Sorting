#!/usr/bin/env python

"""lab0x02.py: implementations of sorting algorithms"""
__author__ = "Jessica Lynch"

from classes.string_list import StringList 
import timeit
from time import perf_counter_ns 

def main():
    try:
        N = 1000
        k = 10
        min_v = 1
        max_v = 256

        strings = StringList(N, k, min_v, max_v)
        #strings.print()
        #strings.verify_sorts()

        #strings.radix_sort(debug=True)
        #print(strings.is_sorted())

        strings.verify_sorts()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()