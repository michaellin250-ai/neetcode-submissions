class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_set = {}

        for i, number in enumerate(nums):
            difference = target - number
            if difference in prev_set:
                return [prev_set[difference], i]
            prev_set[number] = i