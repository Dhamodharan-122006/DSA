class Solution:
    def minOperations(self, n: int) -> int:
        arr = [0]*n
        for i in range(0,n):
            arr[i] = (2*i) + 1
        target = sum(arr)/n
        s = 0
        for i in range(len(arr)):
            if arr[i] <= target:
                s = s + (target-arr[i])
        return int(s)