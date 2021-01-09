#! python3
# step_4.py
""" STEP-4 
This script was made for learning how to optimize our python code.

It reads data from two .txt files, and prints the
number of lines which are same in both the .txt files.

This script requires that `pandas` be installed within the Python
environment you are running this script in.
"""

import time
import pandas as pd
import numpy as np

def openFiles():
    """Open two text files and stores each line in the of that file in a list
    Parameters:
    --------------
    None

    Returns:
    -------------
    subset_elements : list 
        a list of strings from subset_elemets.txt
    all_elements : list 
        a list of strings from subset_elements.txt
    """

    with open('subset_elemets.txt') as f:
        subset_elements = f.read().split('\n')
    
    with open('all_elements.txt') as f:
        all_elements = f.read().split('\n')
    return subset_elements,all_elements

def appendOldWay(subset_elements,all_elements):
    """Prints a list of elements and time taken to execute this function.

    This function uses nested for loops and append() method to find the elements 
    which are present in both the lists passed as arguments, and stores them in a
    new list. It prints the length of the new list along with time taken by this 
    function. 
    
    Parameters:
    --------------
    subset_elements : list
        a list of strings 
    all_elements : list
        a list of strings
    Returns:
    -------------
    None
    """
    start = time.time()
    verified_elements = []
    for element in subset_elements:
        if element in all_elements:
            verified_elements.append(element)
    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))

def appendNumPy(subset_elements, all_elements):
    """Prints a list of elements and time taken to execute this function.

    This function uses NumPy methods to find the elements which are present
    in both the lists passed as arguments, and stores them in a new list. 
    It prints the length of the new list along with time taken by this 
    function. 
    
    Parameters:
    --------------
    subset_elements : list
        a list of strings 
    all_elements : list
        a list of strings
    Returns:
    -------------
    None
    """

    start = time.time()
    subsetArr=np.array(subset_elements)
    allArr=np.array(all_elements)
    verified_elements = np.array([])
    verified_elements=np.intersect1d(subsetArr,allArr)
    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))

def appendDataStruct(subset_elements,all_elements):
    """Prints a list of elements and time taken to execute this function.

    This function use of python data structures and set() method to find 
    the elements which are present in both the lists passed as arguments,
    and stores them in a new list. It prints the length of the new list along
     with time taken by this 
    function. 
    
    Parameters:
    --------------
    subset_elements : list
        a list of strings 
    all_elements : list
        a list of strings
    Returns:
    -------------
    None
    """

    start = time.time()
    verified_elements = list(set(subset_elements)&set(all_elements))
    print(len(verified_elements))
    print(f'Duration: {time.time() - start} seconds')

def main():
    subset_elements, all_elements=openFiles()
    print('When Using old code with for loop--->')
    appendOldWay(subset_elements,all_elements)
    print("when using NumPy module's methods--->")
    appendNumPy(subset_elements,all_elements)
    print("When using python data structure's methods(sets)--->")
    appendDataStruct(subset_elements,all_elements)

if __name__=="__main__":
    main()