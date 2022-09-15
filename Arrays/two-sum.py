class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2, 7, 11, 15, target = 9
        
        
        results = {}
        for i in range(len(nums)):
            num = nums[i]
            key = target - num
            if key in results:
                return [results[key], i]
            results[num] = i
        
        
            
# Tests
ans = Solution()
print(ans.twoSum([2, 7, 11, 15], 9)) # expected: [0, 1]
print(ans.twoSum([3, 2, 4], 6))      # expected: [1, 2]
print(ans.twoSum([3, 3], 6))         # expected: [0, 1]
