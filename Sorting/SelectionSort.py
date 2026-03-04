class Solution:
    def asc(self, items_list):
        length = len(items_list)

        for i in range(length):
            least = i
            for j in range(i+1, length):
                if items_list[j] < items_list[least] :
                    least = j
            if least != i:
                # items_list[i] = items_list[least] + items_list[i]
                # items_list[least] = items_list[i] - items_list[least]
                # items_list[i] = items_list[i] - items_list[least]
                ## Python easy swap
                items_list[i], items_list[least] = items_list[least], items_list[i]
            print(items_list[i])
    
    def desc(self, items_list):
        length = len(items_list)

        for i in range(length):
            max = i
            for j in range(i+1, length):
                if items_list[j] > items_list[max] :
                    max = j
            if max != i:
                ## Python easy swap
                items_list[i], items_list[max] = items_list[max], items_list[i]
            print(items_list[i])

sol = Solution()
nums_list = [5, 7, 8, 1, 4, 6, 9, 2]
print("\nasc sort: ")
sol.asc(nums_list)
print("\ndesc sort: ")
sol.desc(nums_list)
