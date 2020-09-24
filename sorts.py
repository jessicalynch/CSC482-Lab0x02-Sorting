#!/usr/bin/env python

"""sorts.py: Sorting functions"""
__author__ = "Jessica Lynch"

import random
from time import perf_counter_ns
import math

def generate_test_list(N, k, min_v, max_v):
    """Generate a list of strings"""
    if min_v < 1 or max_v > 256:
        raise ValueError("generate_test_list failed: min/max out of ASCII range")
    return [''.join(chr(random.randint(min_v, max_v)) for _ in range(k)) for _ in range(N)]

def is_sorted(L):
    """Checks if a list is in ascending order

    Parameters:
    arg1 (list): a list to scan

    Returns: 
    bool: if the list is sorted or not
    """
    # Iterate through the list
    for i in range(len(L) - 1):
        # Return False if any value is found 
        # to be larger than its predecessor
        if L[i+1] < L[i]:
            return False
    return True # Made it all the way through the list

def verify_sorts(N, k, min_v, max_v):
    """Verify that all sorts are working correctly"""
    # Add all sorting functions to a list
    sorting_functions = [bubble_sort, selection_sort, insertion_sort, radix_sort, counting_sort, merge_sort, quicksort]

    # Generate a list of strings for each sorting function
    # and test if the function sorts correctly
    for sf in sorting_functions:
        SORT_NAME = sf.__name__
        print(f"Generating list of length {N}, key width of {k}")
        L = generate_test_list(N, k, min_v, max_v)
        print(f"Sorting with {(SORT_NAME).upper().replace('_', ' ')}")
        # print(L)
        if SORT_NAME == 'quicksort':
            L = sf(L, 0, len(L)-1)
        else:
            L = sf(L)
        # print(L)
        print("Verifying...", "Sorted!" if is_sorted(L) else "Failed!", end="\n\n")

def bubble_sort(L):
    """An elementary sorting algorithm

    Parameters:
    arg1 (list): a list to be sorted

    Returns: 
    list: a sorted list
    """
    N = len(L)

    # For each pass through the list
    # the largest value bubbles to the top (end)
    for i in range(N-1):

        # Inner loop shrinks with each pass
        # as the values at the end are already sorted
        for j in range(N-1-i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]

    return L

def counting_sort(L, debug=False):
    # Init dictionary with keys for each 
    # unique value in the list
    counter = dict.fromkeys(L, 0)
    if len(counter) > 1000:
        raise ValueError("Counting sort: too many keys")

    # Put keys in order
    ordered_keys = sorted(counter)

    # Pass through list and increment counter
    for val in L:
        counter[val] += 1

    # Reassemble the list in order 
    # using dictionary keys and quantities
    current_index = 0
    for key in ordered_keys:
        qty = counter[key]
        for _ in range(int(qty)):
            L[current_index] = key
            current_index += 1
    return L

def insertion_sort(L, debug=False):
    """An elementary sorting algorithm

    Parameters:
    arg1 (list): a list to be sorted

    Returns: 
    list: a sorted list
    """    
    # Iterate forward through the list
    for i in range(1, len(L)):
        # Start inner loop at i and move backward
        j = i
        # Swap element with its predecessor if
        # the predecessor value is larger
        while j > 0 and L[j] < L[j-1]:
            L[j-1], L[j] = L[j], L[j-1]
            j -= 1
    return L

def merge(L1, L2, debug=False):
    """A helper function for Merge Sort that combines two lists into one
    in ascending order

    Parameters:
    arg1 (list): first list
    arg2 (list): second list
    arg3 (bool): prints steps if true 

    Returns: 
    list: a single sorted list
    """        
    if debug:
        print("\tmerge: ", L1, L2)

    # Init new list 
    merged_list = []

    # While both list halves contain elements,
    # compare the first index of each and
    # pop the smallest value into the new list
    while len(L1) > 0 and len(L2) > 0:
        if L1[0] < L2[0]:
            merged_list += L1.pop(0)
        else:
            merged_list += L2.pop(0)

    # When only one half contains elements,
    # attach it to the end of the new list
    if len(L1) > 0:
        merged_list += L1
    elif len(L2) > 0:
        merged_list += L2

    if debug:
        print("\tmerged_list: ", merged_list)
    
    return merged_list

def merge_sort(L, debug=False):
    """A divide-and-conquer sorting algorithm that recursively divides 
    a list in half until it consists of only a single element
    and uses helper function to reassemble

    Parameters:
    arg1 (list): a list to be sorted
    arg2 (bool): prints steps if true 

    Returns: 
    list: a sorted list
    """    
    if debug:
        print("merge_sort: ", L)

    # Base case: when list contains only one element
    if len(L) <= 1:
        return L

    # Divide the list into two halves
    mid = len(L) // 2
    L1 = L[:mid]
    L2 = L[mid:]

    # Recursive call on each half
    L1 = merge_sort(L1)
    L2 = merge_sort(L2)

    return merge(L1, L2)

def partition(L, start, end, debug=False):
    """A helper function for quicksort that uses the last element 
    of the current list as a pivot value 
    and moves all smaller elements to the left

    Parameters:
    arg1 (list): a list to be sorted
    arg2 (int): starting index
    arg3 (int): ending index
    arg4 (bool): prints steps if true 

    Returns: 
    int: index of the pivot value
    """    
    if debug:
        print(f"\tpartition: start = {start}, end = {end}")
        print("\t", end="")
        print(L[start:end+1])

    i = start-1 # track pivot index
    
    # Compare each value in list to the value
    # at the last index (end)
    for j in range(start, end):

        # If value is found larger than L[end]
        # it is moved to the left and i is incremented
        if (L[j] <= L[end]):
            i += 1
            L[i], L[j] = L[j], L[i]

    # Value at last index is placed after the last element 
    # found to be smaller, and it becomes the pivot index.
    # All values left of pivot index are smaller than pivot value
    L[i+1], L[end] = L[end], L[i+1]

    if debug:
        print(f"\tRETURN: pivot = {i+1}")

    # Return pivot index    
    return i+1

def quicksort(L, start, end, debug=False):
    """A divide-and-conquer sorting algorithm that recursively partitions 
    a list into two parts, with all elements left of pivot index
    smaller than pivot value

    Parameters:
    arg1 (list): a list to be sorted
    arg2 (int): starting index
    arg3 (int): ending index
    arg4 (bool): prints steps if true 

    Returns: 
    list: a sorted list
    """
    if debug:
        print(f"quicksort: start = {start}, end = {end}")

    # The first call to quicksort uses the first and last indecies 
    # of the complete list for start and end values
    if (start < end):
        pivot = partition(L, start, end, debug)
        quicksort(L, start, pivot-1, debug)
        quicksort(L, pivot+1, end, debug)
    return L

def radix_sort(inputL, d=1, debug=False):
    """A comparison-free sorting algorithm

    Parameters:
    arg1 (list): a list to be sorted
    arg2 (int): segment size
    arg3 (bool): prints steps if true 

    Returns: 
    list: a sorted list
    """
    # Init output list with same length as input
    outputL = [0] * len(inputL)

    # Get the length of the strings
    k = len(inputL[0])

    # Determine if segment size is valid
    if d != 1:
        raise ValueError("TODO: handle larger d values")
    # if d > k:
    #     raise ValueError("Radix sort: d must be smaller than k")

    # Calculate number of buckets needed based on segment size (d)
    num_buckets = (2**8) ** d
    num_segments = k // d
    
    # Cycle through the segments of each string
    for i in range(num_segments):
        # Init counter
        counts = [0] * (num_buckets + 1)

        # Increment counter
        for string in inputL:
            counts[ord(string[num_segments-i-1])] += 1

        # Calculate prefix sum
        for x in range(1, len(counts)):
            counts[x] += counts[x-1]
        
        # Rebuild list
        for string in reversed(inputL):
            x = ord(string[num_segments-i-1])
            counts[x] -= 1
            outputL[counts[x]] = string

        # Copy values from output list to input list    
        inputL = outputL.copy()

    return inputL

def find_min(L, start, debug=False):
    """A helper function for selection_sort

    Parameters:
    arg1 (list): a list to be sorted
    arg2 (int):  index to start searching from
    arg3 (bool): prints steps if true 

    Returns: 
    int: index of the smallest value
    """
    # Save value at starting index    
    min_value = L[start]
    min_loc = start

    # Pass through the list looking for smaller values
    for i in range(start, len(L)):
        if L[i] < min_value:
            min_value = L[i]
            min_loc = i
    return min_loc

def selection_sort(L, debug=False):    
    """An elementary sort where the smallest value is 
    continually moved to the beginning of the list

    Parameters:
    arg1 (list): a list to be sorted
    arg2 (bool): prints steps if true 

    Returns: 
    list: a sorted list
    """
    # Pass through the list
    for i in range(len(L)):
        # Find the smallest value on each pass
        # and move to the left
        min_loc = find_min(L, i, debug)
        if L[i] != L[min_loc]:
            L[i], L[min_loc] = L[min_loc], L[i]
    return L