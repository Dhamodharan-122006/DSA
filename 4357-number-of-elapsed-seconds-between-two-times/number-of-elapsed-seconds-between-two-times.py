class Solution:
    def secondsBetweenTimes(self, s: str, e: str) -> int:
        start = s.split(':')
        end = e.split(':')
        s_time = int(start[0])*3600 + int(start[1])*60 + int(start[2])
        e_time = int(end[0])*3600 + int(end[1])*60 + int(end[2])
        return abs(s_time - e_time)
        