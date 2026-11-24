class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = zip(position, speed)
        pos_speed = sorted(pos_speed, reverse=True)

        s = []
        
        for car in pos_speed:
            t = (target - car[0])/car[1]

            if len(s) == 0:
                s.append(t)
            else:
                if t > s[-1]:
                    s.append(t)
            #if len(s) > 1 and s[-1] <= s[-2]:
            #    s.pop()

        
        return len(s)