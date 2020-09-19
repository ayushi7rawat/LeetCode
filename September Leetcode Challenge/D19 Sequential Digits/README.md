Sequential Digits
==========================

![alt text](https://github.com/ayushi7rawat/LeetCode/blob/master/September%20Leetcode%20Challenge/D18%20Best%20Time%20to%20Buy%20and%20Sell%20Stock/cover.jpg)

Explanation Walkthrough:
==========================
*You can find a complete step by step explanation walkthrough at my september Leetcode challenge* [Youtube Playlist](https://www.youtube.com/playlist?list=PLjaO05BrsbIP4_rYhYjB95q-IpxoIXmlm)

Problem Statement:
==========================
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:
==========================
```
Input: low = 100, high = 300
Output: [123,234]
```

Example 2:
==========================
```
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
```

Constraints:
==========================
```
10 <= low <= high <= 10^9
```

Hint 1:
==========================
```
Generate all numbers with sequential digits and check if they are in the given range.
```

Hint 2:
==========================
```
Fix the starting digit then do a recursion that tries to append all valid digits.
```