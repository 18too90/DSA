class Solution:
    def asc(self, series):
        length = len(series)

        for i in range(length):
            is_swap = False
            for j in range(length-i-1):
                if series[j]> series[j+1]:
                    series[j],series[j+1] = series[j+1], series[j]
                    is_swap = True
            if(is_swap == False):
                break
            print(series)

    def desc(self, series):
        length = len(series)
        for i in range(length-1, -1, -1):
            is_swap = False
            for j in range(i):
                if series[j]< series[j+1]:
                    series[j],series[j+1] = series[j+1], series[j]
                    is_swap = True   
            if(is_swap == False):
                break
            print(series)
sol = Solution()
print("\nAscending:")
sol.asc([5, 8, 1, 6, 9, 2, 4])

print("\nDescending:")
sol.desc([5, 8, 1, 6, 9, 2, 4])