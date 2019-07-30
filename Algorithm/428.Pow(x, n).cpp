/*
 * @lc app=leetcode id=50 lang=cpp
 *
 * [50] Pow(x, n)
 */
class Solution
{
public:
    double myPow(double x, int n)
    {
        if (n == 0)
        {
            return 1;
        }
        if (n == 1)
        {
            return x;
        }
        int t = n / 2;
        if (n < 0)
        {
            t = -t;
            x = 1 / x;
        }

        if (n % 2 == 0)
        {
            return myPow(x * x, t);
        }
        else
        {
            return myPow(x * x, t) * x;
        }
    }
};
