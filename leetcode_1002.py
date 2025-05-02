class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        comman=list(words[0])
        for word in words[1:]:
            temp=[]
            for char in word:
                if char in comman:
                    temp.append(char)
                    comman.remove(char)
            comman=temp
            
        return comman
