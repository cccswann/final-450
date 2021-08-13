### Maximum and minimum of an array using minimum number of comparisons ###

## Linear Search
# Values min and max. Compare each element with min and max,
# change min and max accordingly

class pair:
    def __init__(self):
        self.min = 0 
        self.max = 0
    
def getMinMax(arr: list, n: int) -> pair:
    minmax = pair()

    if n == 1:
        minmax.max = arr[0]
        minmax.min = arr[0]
        return minmax
    
    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]
    
    # Start at 3
    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]
    
    return minmax

# Driver Code

arr1 = [1000, 11, 445, 1, 330, 3000]
arr_size = 6
minmax = getMinMax(arr1, arr_size)
print("Min is", minmax.min)
print("Max is", minmax.max)

## Another approach
# Divide into two parts and compare the min and max of two parts 

def getMinMax2(low, high, arr):
    arr_max = arr[low]
    arr_min = arr[low]
    # One element
    if low == high:
        arr_max = arr[low]
        arr_min = arr[low]
        return (arr_max, arr_min)
    # Two elements
    elif high == low + 1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[low]
        return (arr_max, arr_min)
    
    else:
        mid = int((low + high) / 2)
        arr_max1, arr_min1 = getMinMax2(low, mid, arr)
        arr_max2, arr_min2 =  getMinMax2(mid+1, high, arr)
    return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))

# Driver code
arr2 = [1000, 11, 445, 1, 330, 3000]
high = len(arr2) - 1
low = 0
arr_max, arr_min = getMinMax(low, high, arr2)
print('Min element is ', arr_min)
print('Max element is ', arr_max)