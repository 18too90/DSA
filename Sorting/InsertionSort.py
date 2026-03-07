class Solution:
    def asc_sort(self, series):
        length = len(series)
        print(series)
        for i in range(1, length):
            key = series[i]
            j = i-1
            while j >= 0 and series[j] > key:
                series[j+1] = series[j]
                j = j-1 
                print(series)
            series[j+1] = key 
            print(series)
    def desc_sort(self, series):
        length = len(series)
        for i in range(1,length):
            key = series[i]
            j = i-1
            while j>=0 and series[j] < key:
                series[j+1] = series[j]
                j = j-1
                print(series)
            series[j+1] = key
            print(series)

sol = Solution()
print("\nAscending Order:")
sol.asc_sort([3, 5, 4, 6, 8, 9, 7, 10, 1])
print("\nDescending Order:")
sol.desc_sort([3, 5, 4, 6, 8, 9, 7, 10, 1])