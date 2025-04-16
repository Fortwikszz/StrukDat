class Solution:
    def longestWPI(self, hours: list) -> int:
        sumtin = 0
        interval = 0
        tracked = {}
        for i in range(len(hours)):
            if hours [i] > 8:
                sumtin += 1
            else:
                sumtin -= 1
            
            if sumtin > 0:
                interval = i + 1
            else:
                if sumtin - 1 in tracked:
                    interval = max(interval, i - tracked[sumtin - 1])
        
            if sumtin not in tracked:
                tracked[sumtin] = i

        return interval