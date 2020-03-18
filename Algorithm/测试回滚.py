# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
import collections


class Solution:
    def longestPalindrome(self, s):
        d = collections.defaultdict(int)
        for char in s:
            d[char] += 1

        hasOdd = False
        res = 0
        for v in d.values():
            if v % 2 == 0:
                res += v
            elif v > 1:
                res += v - 1
                hasOdd = True
            else:
                hasOdd = True

        if hasOdd:
            res += 1

        return res

