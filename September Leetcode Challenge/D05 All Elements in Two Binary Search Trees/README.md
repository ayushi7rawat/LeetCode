All Elements in Two Binary Search Trees
==========================

![alt text](
https://github.com/ayushi7rawat/LeetCode/blob/master/September%20Leetcode%20Challenge/S_D05_All%20Elements%20in%20Two%20Binary%20Search%20Trees/cover.jpg)

Explanation Walkthrough:
==========================
*You can find a complete step by step explanation walkthrough at my september Leetcode challenge* [Youtube Playlist](https://www.youtube.com/playlist?list=PLjaO05BrsbIP4_rYhYjB95q-IpxoIXmlm)

Problem Statement:
==========================
Given two binary search trees root1 and root2.
Return a list containing all the integers from both trees sorted in ascending order.

---
Example 1
==========================
```
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
```

Example 2
==========================
```
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]
```

Example 3
==========================
```
Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]
```

Example 4
==========================
```
Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]
```

Example 5
==========================
```
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
```

Constraints:
==========================
```
Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].
```

Hint #1  
==========================
```
Traverse the first tree in list1 and the second tree in list2.
```

Hint #2 
==========================
```
Merge the two trees in one list and sort it.
```
