class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevMap = {}; # Hashmap for previously traversed elements
        for i, n in enumerate(nums):
            target = n
            if target in prevMap:
                return True
            else:
                prevMap[n] = i   
        return False