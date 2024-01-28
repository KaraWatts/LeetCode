class Solution:
    def containsDuplicate(self, nums) -> bool:
        if len(nums) <= 1:
            return False
        numsDict = {}

        for num in nums:
            if num in numsDict:
                return True
            else: 
                numsDict[num] = 1
        return False
    

print(Solution().containsDuplicate(nums =[1,2,3,1])) ## True
print(Solution().containsDuplicate(nums =[1,2,3,4])) ## False