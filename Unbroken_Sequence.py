# -*- coding: utf-8 -*-
"""
Consider and array of integers, A. An integer m is defined as the size of some
subsequence, s, where each element covers an unbroken range of integers.
That is to say, if you were to sort the elements in s, the absolute difference
between elements j,j+1 would be zero or 1. Determine the maximum length of a subsequence chosen form A
"""

def longest_sequence(A):
    A.sort() # O(nlogn)

    m = 0
    tmp = 0
    for j in range(1,len(A)):
        diff = A[j] - A[j-1]
        if diff == 0 or diff == 1:
            tmp +=  1
            m = max(m,tmp)
        else: tmp = 0            
        
    return m + 1 
    

def main():
    tests = [[8,5,4,8,4]]
    for test in tests:
         print(longest_sequence(test))
    
if __name__ == '__main__':
    main()