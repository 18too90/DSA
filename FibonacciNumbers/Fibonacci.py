class Solution:
    def func(self, index):
        if index == 0 or index == 1:
            return index
        return self.func(index-1) + self.func(index-2)
    
    def fib (self, index:int) -> int:
        answer = self.func(index)
        return answer
    
sol = Solution()
print("Printing first 10 numbers of fibonacci series below:")
for x in range(10):
    print(sol.fib(x))