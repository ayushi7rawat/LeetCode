Robot Bounded In Circle
==========================

![alt text](https://github.com/ayushi7rawat/LeetCode/blob/master/September%20Leetcode%20Challenge/D17%20Robot%20Bounded%20In%20Circle/cover.jpg)

Explanation Walkthrough:
==========================
*You can find a complete step by step explanation walkthrough at my september Leetcode challenge* [Youtube Playlist](https://www.youtube.com/playlist?list=PLjaO05BrsbIP4_rYhYjB95q-IpxoIXmlm)

Problem Statement:
==========================
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:
==========================
```
Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
```

Example 2:
==========================
```
Input: "GG"
Output: false
Explanation: 
The robot moves north indefinitely.
```

Example 3:
==========================
```
Input: "GL"
Output: true
Explanation: 
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
```

Note:
==========================
```
1. 1 <= instructions.length <= 100
2. instructions[i] is in {'G', 'L', 'R'}
```

Hint 1:
==========================
```
Calculate the final vector of how the robot travels after executing all instructions once - it consists of a change in position plus a change in direction.
```

Hint 2:
==========================
```
The robot stays in the circle iff (looking at the final vector) it changes direction (ie. doesn't stay pointing north), or it moves 0.
```