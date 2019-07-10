#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = "#".join(s)
        s = "#" + s + "#"
        length = len(s)
        if length == 0:
            return ""

        maxL = 1
        res = s[0]
        for i in range(length):
            left = i
            right = i

            while right + 1 < length and left - 1 >= 0:
                right += 1
                left -= 1
                if s[left] == s[right]:
                    if right - left + 1 > maxL:
                        maxL = right - left + 1
                        res = s[left : right + 1]
                else:
                    break

        return "".join(res.split("#"))

