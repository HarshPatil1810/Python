class Solution(object):
    from collections import Counter 
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        required_count=Counter(c.lower() for c in licensePlate if c.isalpha() )

        words.sort(key=len)
        for word in words:
            word_counts=Counter(word)
            if all(word_counts[char] >= required_count[char] for char in            required_count):
                return word
