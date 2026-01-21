class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        result = [0 if x % 2 == 0 else 1 for x in nums]
        result.sort()
        return result