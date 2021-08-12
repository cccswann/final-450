# Reverse a String Problem
# https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
# Implemented in practice first. Reverse a string.

# Iterative Approach

def reverseWord(s):
    # Change string to list - strings are immutable in python
    list1 = list(s)
    # Create 2 pointers - start and end
    start = 0 
    end = len(list1) - 1
    # In a loop swap the start with the end pointer 
    while start < end:
        list1[start], list1[end] = list1[end], list1[start]
        start += 1
        end -= 1
    # Revert list back to string 
    str1 = ''.join(list1) 
    return str1