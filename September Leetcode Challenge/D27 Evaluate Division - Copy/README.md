Subarray Product Less Than K
==========================

![alt text](https://github.com/ayushi7rawat/LeetCode/blob/master/September%20Leetcode%20Challenge/D27%20Evaluate%20Division/cover.jpg)

Explanation Walkthrough:
==========================
*You can find a complete step by step explanation walkthrough at my september Leetcode challenge* [Youtube Playlist](https://www.youtube.com/playlist?list=PLjaO05BrsbIP4_rYhYjB95q-IpxoIXmlm)

Problem Statement:
==========================
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
==========================
```
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
```

Note:
==========================
```
0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
```

Hint:
==========================
```
For each j, let opt(j) be the smallest i so that nums[i] * nums[i+1] * ... * nums[j] is less than k. opt is an increasing function.
```