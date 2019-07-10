/*
 * @lc app=leetcode id=852 lang=c
 *
 * [852] Peak Index in a Mountain Array
 */

int peakIndexInMountainArray(int *A, int ASize)
{
    if (ASize == 0)
    {
        return 0;
    }
    int peakIndex = 0;
    int peak = A[0];
    for (int i = 1; i < ASize; i++)
    {
        if (A[i] > peak)
        {
            peak = A[i];
            peakIndex = i;
        }
    }
    return peakIndex;
}
