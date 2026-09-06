class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        maximum = []
        for i in range(len(score)):
            maximum.append(score[i][k])
        maximum.sort(reverse = True)
        print(maximum)
        result = []
        for i in range(len(maximum)):
            for row in score:
                if maximum[i] in row:
                    result.append(row)
        return result
        