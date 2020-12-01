class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # first we should take the list of integers and sort them in reverse
        # nums_sort = sorted(nums)
        # now we simply take the top four numbers, add them, and add them once more for our output
        #         counter = 0
        #         value = 0
        #         while counter < len(nums):
        #             value += min(nums[counter], nums[counter+2])
        #             counter += 1

        #         return value
        return sum(sorted(nums)[::2])
