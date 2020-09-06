Contains Duplicate III
==========================

![alt text](https://github.com/ayushi7rawat/LeetCode/blob/master/September%20Leetcode%20Challenge/S_D01_LargestTimeforGivenDigits/cover.jpg)

Explanation Walkthrough:
==========================
*You can find a complete step by step explanation walkthrough at my september Leetcode challenge* [Youtube Playlist](https://www.youtube.com/playlist?list=PLjaO05BrsbIP4_rYhYjB95q-IpxoIXmlm)

Problem Statement:
==========================
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
 
---
Example 1
==========================
```
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
```

Example 2
==========================
```
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
```

Example 3
==========================
```
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
```
Show Hint #1:
```
Time complexity O(n logk) - This will give an indication that sorting is involved for k elements.
```
Show Hint #1:
```
Use already existing state to evaluate next state - Like, a set of k sorted numbers are only needed to be tracked.
When we are processing the next number in array, then we can utilize the existing sorted state and it is not necessary to sort next
overlapping set of k numbers again.
```