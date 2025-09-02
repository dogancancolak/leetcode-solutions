class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        if len(words) == 1:
            return True
        letter_counts = dict()

        for word in words:
            for letter in word:
                letter_counts[letter] = letter_counts.get(letter,0)+1
        return all([count % len(words) == 0 for letter,count in letter_counts.items()])