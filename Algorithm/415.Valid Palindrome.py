#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
import math
import re


class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        s = "".join(re.findall(r"[a-zA-Z0-9]", s))
        lenth = len(s)

        for i in range(math.ceil(lenth / 2)):
            if s[i] != s[lenth - 1 - i]:
                return False

        return True

