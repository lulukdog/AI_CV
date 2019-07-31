/*
 * @lc app=leetcode id=153 lang=cpp
 *
 * [153] Find Minimum in Rotated Sorted Array
 */
#include <vector>
using namespace std;

class Solution
{
public:
    int findMin(vector<int> &nums)
    {
        int left = 0;
        int right = nums.size();
        int res = nums[0];
        while (left < right - 1)
        {
            int mid = left + (right - left) / 2;
            if (nums[mid] < nums[left])
            {
                right = mid;
            }
            else
            {
                left = mid;
            }
            if (nums[mid] < nums[0])
            {
                res = nums[mid];
            }
        }
        return res;
    }
};
