class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for idx, i in enumerate(nums):
            m = target - i
            if m in seen:
                return [seen[m], idx]
            else:
                seen[i] = idx