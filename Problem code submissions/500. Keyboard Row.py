class Solution:
#500. Keyboard Row
    def findWords(self, words: List[str]) -> List[str]:
        a, b, c = 'qwertyuiop', 'asdfghjkl', 'zxcvbnm'
        res =[]
        
        for word in words:
            counter1, counter2, counter3 = 0, 0, 0
            
            for i in word:
                if i.lower() in a:
                    counter1 += 1
                elif i.lower() in b:
                    counter2 += 1
                elif i.lower() in c:
                    counter3 += 1

            if counter1 == len(word) or counter2 == len(word) or counter3 == len(word):
                res.append(word)
        return res
