"""
441. Arranging Coins
https://leetcode.com/problems/arranging-coins/

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)


assert Solution().arrangeCoins(5) == 2
assert Solution().arrangeCoins(8) == 3
