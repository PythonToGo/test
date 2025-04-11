class Solution:class Solution:
    def twoSum(self, nums: list[int], target: int) -> list    def twoSum(self, nums: list[int], target: int) -> list
[int]:[int]:
        numToIndex = {}        numToIndex = {}

        for i, num in enumerate(nums):        for i, num in enumerate(nums):
            if target - num in numToIndex:            if target - num in numToIndex:
                return numToIndex[target - num], i                return numToIndex[target - num], i
            numToIndex[num] = i            numToIndex[num] = i
