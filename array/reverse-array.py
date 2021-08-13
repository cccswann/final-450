### REVERSE ARRAY ###

## Iterative Approach
# Start and end indexes at 0 and n-1 respectively
# In a loop, swap arr[end] with arr[start]
# Change start and end. Start + 1 and End - 1 

def reverseList(A):
    start = 0
    end = len(A)-1

    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
    
    return A

## Recursive Approach
# Initialize start and end indexes at start = 0, end = n-1
# Swap arr[start] with arr[end]
# Recursively call reverse for rest of the array

def reverseList2(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList2(A, start+1, end-1)

A = [1,2,3,4,5,6]
reverseList2(A, 0, 5)
print("Reversed array is:")
print(A)

## List Slice Approach

def reverseList3(A):
    newArr = A[::-1]
    return newArr