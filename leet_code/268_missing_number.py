"""
https://leetcode.com/problems/missing-number/
268. Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        record = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            record[nums[i]] = 1
        for i in range(len(record)):
            if record[i] == 0:
                return i
