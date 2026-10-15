class TimeMap:

    def __init__(self):
        self.hmap = {} #key = key, value = [(timestamp1, value), (timestamp2, value), ... , (timestampx, value)]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hmap:
            self.hmap[key].append((timestamp, value))
        else:
            self.hmap[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            #does not exist
            return ""
        if self.hmap[key][0][0] > timestamp:
            #if the earliest timestamp set is greater than what is being got, there is no valid timestamp
            return ""
        
        values = self.hmap[key]
        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2

            if values[mid][0] == timestamp:
                return values[mid][1]
            
            if values[mid][0] > timestamp:
                #timestamp is too large
                right = mid - 1
            else:
                #timestamp too small, valid but can we do better(get closer to timestamp wanted)
                left = mid + 1

        #once left and right cross over right is right-most valid timestamp
        return values[right][1]