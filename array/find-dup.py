### Find the Duplicate Number ###

## Using Counter from collections library

def findDuplicate(self, nums: List[int]) -> int:
    new = Counter(nums)
    list1 = [str(item) for item in new if new[item] > 1]
    dup = ''.join(list1)
    dupInt = int(dup)
    return dup

## Using set

def findDuplicate2(self, nums: List[int]) -> int:
    new = set()
    for num in nums:
        if num in new:
            return num
        new.add(num)
        