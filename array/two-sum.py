### Two Sum ###
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

def findTwoSum(nums, target):
    # Create hashmap
    hashmap = {}
    for i in range(len(nums)):
        # Create a complement
        complement = target - nums[i]
        # If complement exists in hashmap return the two indices
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i 













