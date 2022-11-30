class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xors = functools.reduce(operator.xor, nums)
        low = xors & -xors
        res = [0, 0]
        
        for num in nums:
            if num & low:
                res[0] ^= num
            else:
                res[1] ^= num
        return res
