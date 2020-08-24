# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a hashtable to put all ints into
        cache = {}
        # Go through each int in the list
        for int in nums:
            if int not in cache:
                cache[int] = 1
            else:
                # if it already exists in the cache return true
                return True
        # if we run through the whole list and no dupes, return false
        return False


TestList = [1, 2, 3, 1]

Solution.containsDuplicate(TestList)
