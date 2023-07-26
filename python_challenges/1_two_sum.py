from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_hash = {}
        if not nums:
            return []
        for i, num in enumerate(nums):
            result = target - num
            if num in sum_hash.keys():
                return [i, sum_hash[num]]
            else:
                sum_hash[result] = i
        return []
