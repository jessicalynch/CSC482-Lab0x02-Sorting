#!/usr/bin/env python

"""lab0x02.py: implementations of sorting algorithms"""
__author__ = "Jessica Lynch"

from classes.integer_list import IntegerList 
import timeit
from time import perf_counter_ns 

def main():
    try:
        # data = IntegerList()
        data = IntegerList("data/4Kints.txt")
        # data.gen_ints(1000000, 0, 10000)
        # data.bubble_sort()
        # data.merge_sort()
        data.quick_sort(debug=False)
        # print(data.values)
        print(data.is_sorted())
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()