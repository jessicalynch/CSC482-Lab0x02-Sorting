#!/usr/bin/env python

"""lab0x02.py: implementations of sorting algorithms"""
__author__ = "Jessica Lynch"

import sorts
from time import perf_counter_ns
import math
import sys

def main():

    try:

        # Verify sorting functions work correctly
        N = 1000
        k = 16
        min_v = 97
        max_v = 122
        sorts.verify_sorts(N, k, min_v, max_v)

        # Assign timer function to variable
        clock = perf_counter_ns

        # Determine max run time for each algorithm
        one_second = 1000000000 # 1 second in nanoseconds
        MAX_RUN_TIME = one_second * 60

        # Init string constants for table header
        t_str = "Time"
        dr_str = "DR"
        na_str = "na"

        # Build list with sorts to test
        sorting_functions = [sorts.insertion_sort]

        # Test performance of each sorting function in list
        for sf in sorting_functions:

            # Init loop variables 
            # and lists to store table data
            N = 1
            NUM_K = 4
            results = [1] * NUM_K
            doubling_ratio = [1] * NUM_K

            # Get the name of the current sort
            SORT_NAME = sf.__name__

            # Print heading
            print(f"Results for {SORT_NAME}")
            k = 6
            for _ in range(NUM_K):
                print(f"{'k=' + str(k):>30}", end="")
                k *= 2
            print()

            print(f"{'N':>15}", end="")
            for i in range(NUM_K):
                print(f"{t_str:>15}{dr_str:>15.3}", end="")
            print(f"{'Predicted':>15}")
            print()

            timed_out = False # set flag

            # Start collecting table data for lists size of size N,
            # where N doubles each row
            while N < sys.maxsize and timed_out is False:
                timed_out = True
                k = 6
                lists_to_sort = []
                # Generate 4 lists size N
                for i in range(NUM_K):
                    if results[i] > 0:
                        lists_to_sort.append(sorts.generate_test_list(N, k, min_v, max_v))
                        k *= 2
                    else:
                        lists_to_sort.append([])

                for i in range(NUM_K): 
                    if results[i] < 0:
                        continue
                    
                    t0 = clock()
                    L = sf(lists_to_sort[i])
                    t1 = clock() - t0 # time the algorithm took in nanoseconds

                    if N > 1:
                        doubling_ratio[i] = t1 / results[i]
                    else:
                        doubling_ratio[i] = na_str

                    if t1 < MAX_RUN_TIME:
                        timed_out = False # change flag if at least one sort is still going
                        results[i] = t1
                    else:
                        results[i] = -1
                        
                # Calculate predicted doubling ratio
                if N > 1:
                    if SORT_NAME == "merge_sort" or SORT_NAME == "quicksort":
                        if (math.log(int(N/2), 2)) > 0:
                            predicted = math.log(N, 2) / math.log(int(N/2), 2)
                        else:
                            predicted = "nan"                        
                    elif SORT_NAME == "insertion_sort" or SORT_NAME == "bubble_sort" or SORT_NAME == "selection_sort":
                        predicted = N**2 / ((N//2)**2)
                    elif SORT_NAME == "radix_sort":
                        predicted = N / (N//2)
                else:
                    predicted = "na"

                # Print results row for current N value
                print(f"{N:>15}", end="")
                for i in range(NUM_K):
                    print(f"{results[i]:>15}{doubling_ratio[i]:>15.3}" if results[i] > 0  else f"{na_str:>15}{na_str:>15.3}", end="")
                print(f"{predicted:>15.3}")

                N *= 2

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

    