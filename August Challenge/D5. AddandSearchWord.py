class WordDictionary:

    def __init__(self):
        self.words = {}
        

    def addWord(self, word: str) -> None:
        length = len(word)
        if length not in self.words:
            self.words[length] = [word]
        else:
            self.words[length].append(word)
        

    def search(self, word: str) -> bool:
        new_word_length = len(word)
        if new_word_length not in self.words:
            return False
        
        #If we are here then that means we have atleast one word of the same length as our search word
        all_words = self.words[len(word)]
        for i in range(len(all_words)):
            current_word = all_words[i]
            is_present = True
            for j in range(len(current_word)):
                if current_word[j] == word[j] or word[j] == ".":
                    continue
                else:
                    is_present = False
                    break
            if is_present:
                return True  
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)