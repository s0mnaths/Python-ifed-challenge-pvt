#! python3
# step_4.py
""" STEP-4 
This script was made for learning how to optimize our python code.

It reads data from two .txt files, and prints the
number of lines which are same in both the txt files.

This script requires that `pandas` be installed within the Python
environment you are running this script in.
"""

import time
import pandas as pd
import numpy as np

def appendNumpy(arr1,arr2):
    """Returns a list of elements which are present in both the list passed as arguments.

    This function uses NumPy methods to find the elements which are present in both the
    lists passed as arguments, and returns those elements as a list.  
    
    Parameters:
    --------------
    arr1 : list
        a list of strings 
    arr2 : list 
        a list of strings
    Returns:
    -------------
    verified_elements : list
        a list of strings which is which are present in both arr1 and arr2
    """

    subsetArr=np.array(subset_elements)
    allArr=np.array(all_elements)
    verified_elements = np.array([])
    verified_elements=np.intersect1d(subsetArr,allArr)
    return verified_elements

def appendDataStruct(arr1,arr2):
    """Returns a list of elements which are present in both the list passed as arguments.

    This function makes use of python data structures and set() method to find the elements
    which are present in both the lists passed as arguments, and returns those
    elements as a list.  
    
    Parameters:
    --------------
    arr1 : list
        a list of strings 
    arr2 : list 
        a list of strings
    Returns:
    -------------
    verified_elements : list
        a list of strings which is which are present in both arr1 and arr2
    """
    
    verified_elements = list(set(subset_elements)&set(all_elements))
    return verified_elements


with open('subset_elemets.txt') as f:
    subset_elements = f.read().split('\n')
    
with open('all_elements.txt') as f:
    all_elements = f.read().split('\n')

def main():
    start = time.time()
    verified_elements=[]

    #appendNumpy(subset_elements,all_elements)
    appendDataStruct(subset_elements,all_elements)

    print(len(verified_elements))
    print(f'Duration: {time.time() - start} seconds')


if __name__=='__main__':
    main()