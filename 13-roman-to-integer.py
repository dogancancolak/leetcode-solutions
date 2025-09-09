class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sum = 0
        for idx, roman in enumerate(s):
            number = values.get(roman)
            if idx == len(s)-1:
                sum = sum + number
                continue
            if roman == "I" and s[idx+1] in ["V","X"]:
                sum = sum - number
            elif roman == "X" and s[idx+1] in ["L","C"]:
                sum = sum - number
            elif roman == "C" and s[idx+1] in ["D","M"]:
                sum = sum - number
            else:
                sum = sum + number
        return sum