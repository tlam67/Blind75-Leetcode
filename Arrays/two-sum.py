# Given an array of integers, nums, and an interger, target, 
# return indices of the two numbers such that they add up to 
# target.

# You may assume that each input would have exactly one solution
# and you may not use the same element twice.

# You can return the answer in any order.

# Brainstorm:
# Double loop for brute force

from typing import List

# O(n^2)
class Solution: 
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in nums:
      for j in nums:
        if i + j == target:
          return [i, j]

# Tests
ans = Solution()
print(ans.twoSum([2, 7, 11, 15], 9)) # expected: [0, 1]
print(ans.twoSum([3, 2, 4], 6))      # expected: [1, 2]
print(ans.twoSum([3, 3], 6))         # expected: [0, 1]
