class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
        rem = capacity
        step = 0
        for i in range(len(plants)):
            if rem - plants[i] >= 0:
                step += 1
                rem = rem - plants[i]
            else:
                refil = rem + (capacity - rem)
                rem = refil - plants[i]
                step += 2*i+1
        return step

                

        