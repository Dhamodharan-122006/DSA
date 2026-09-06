class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]*(len(encoded)+1)
        for i in range(len(encoded)):
            ans[i+1] = encoded[i] ^ ans[i]
        return ans
        