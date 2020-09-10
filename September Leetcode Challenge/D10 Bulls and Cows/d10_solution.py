class Solution:
'''
Problem Name: Bulls and Cows
Author: Ayushi Rawat
Date: 10-09-2020
'''
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
            new_guess = []
            new_secret = []
            
            for i in range(len(secret)):
                if secret[i] == guess[i]:
                    bulls += 1
                else:
                    new_secret.append(secret[i])
                    new_guess.append(guess[i])
            for key in new_guess:
                if key in new_secret:
                    cows += 1
                    new_secret.remove(key)
            
            return("{}A{}B".format(bulls, cows))
   