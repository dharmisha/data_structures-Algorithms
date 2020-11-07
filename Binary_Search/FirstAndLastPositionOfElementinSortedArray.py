'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
'''
class firstAndLast():
    def __init__(self,nums, target):
        self.nums = nums
        self.target = target
        self.res = []
    def binary_search(self, leftmost = False):
        left = 0
        right = len(self.nums)
        while left<right:
            mid = (left+right)//2
            if self.nums[mid] > self.target or leftmost and self.nums[mid] == self.target:
                right = mid
            else:
                left = mid+1
        return left

    def firstLast(self):
        if not self.nums:
            return [-1,-1]
        leftindex = self.binary_search(True)
        rightindex = self.binary_search(False)
        if leftindex < len(self.nums) and self.nums[leftindex] == self.target and self.nums[rightindex-1]==self.target:
            return [leftindex,rightindex-1]
        else:
            return [-1,-1]
f = firstAndLast([5,7,7,8,8,10], 8)
print(f.firstLast())
f = firstAndLast([5,7,7,8,8,10], 6)
print(f.firstLast())
f = firstAndLast([], 0)
print(f.firstLast())
f = firstAndLast([5,6,6,6,6,6,6,6,7,7,8,8,10], 6)
print(f.firstLast())
f = firstAndLast([1], 1)
print(f.firstLast())
f = firstAndLast([2,2], 3)
print(f.firstLast())
