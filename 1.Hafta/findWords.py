#findWords
class Solution(object):
    def findWords(self, words):
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        result = []
        for i in words:
            wordset = set(i.lower())
            if (wordset.intersection(row1) == wordset): 
                result.append(i)
            elif (wordset.intersection(row2) == wordset):
                result.append(i)
            elif (wordset.intersection(row3) == wordset):
                result.append(i)       
        return result                
