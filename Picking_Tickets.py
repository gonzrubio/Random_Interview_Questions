# -*- coding: utf-8 -*-
"""
Consider and array of integers, A. An integer m 
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