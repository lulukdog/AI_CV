/*
 * @lc app=leetcode id=162 lang=cpp
 *
 * [162] Find Peak Element
 */
#include <vector>

using namespace std;

class Solution
{
public:
    int findPeakElement(vector<int> &nums)
    {
        int peakIndex = 0;
        for (int i = 1; i < nums.size(); i++)
        {
            if (nums[i] > nums[peakIndex])
            {
                peakIndex = i;
            }
            else
            {
                break;
            }
        }
        return peakIndex;
    }
};
