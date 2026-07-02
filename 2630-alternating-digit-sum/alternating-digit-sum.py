class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        l = 0
        for i, digit in enumerate(s):
            if i % 2 == 0:
                l+=int(digit)
            else:
                l -= int(digit)
        return l
        