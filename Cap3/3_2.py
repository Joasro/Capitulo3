from SortArray import *
import random
import timeit

def initArray(size=100, maxValue=100, seed=3.14159):
    """Create an Array of the specified size with a fixed sequence
    of 'random' elements"""
    arr = Array(size) # Create the Array object
    random.seed(seed) # Set random number generator
    for i in range(size): # to known state, then loop
        arr.insert(random.randrange(maxValue)) # Insert random numbers
    return arr # Return the filled Array

arr = initArray()

print("Array containing", len(arr), "items:\n", arr)
arr.insertionSort()
print('Sorted array contains:\n', arr)
print("Valor a la mitad",arr.median())