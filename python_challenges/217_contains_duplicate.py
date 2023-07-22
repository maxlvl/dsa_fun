from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        new_nums = set(nums)
        if len(new_nums) != len(nums):
            return True
        return False
