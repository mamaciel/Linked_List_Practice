class Solution:
    def twoSum(self, nums, target):
        myMap = {}

        for i, j in enumerate(nums):
            diff = target - j
            if diff in myMap:
                return[myMap[diff], i]
            myMap[j] = i
            
m = Solution()
print(m.twoSum([5,2,1,3,7], 5))
