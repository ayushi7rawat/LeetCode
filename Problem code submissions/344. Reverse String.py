class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        head = 0
        tail = len(s)-1

        while tail > head:
            #swap
            s[head], s[tail] = s[tail], s[head]

            #increment pointer
            head += 1
            tail -= 1      