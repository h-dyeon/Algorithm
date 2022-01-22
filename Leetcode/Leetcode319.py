class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n==0:
            return 0
        return int(n**(1/2))