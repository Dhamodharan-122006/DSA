class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        for i in range(len(mat)):
            s += mat[i][i]
        a = 0
        for i in range(len(mat)):
            a += mat[i][len(mat)-1-i]
        print(s,a)
        r = len(mat)
        c = len(mat[0])
        if len(mat) % 2 == 1:
            return s + a - mat[r//2][c//2]
        else:
            return s + a
                