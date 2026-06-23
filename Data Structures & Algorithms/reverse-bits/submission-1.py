class Solution:
    def reverseBits(self, n: int) -> int:
        Res = 0
        for i in range(32):
            Bit = (n >> i) & 1
            Res += (Bit << (31 - i))
        return Res 