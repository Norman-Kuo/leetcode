class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        print(nums, target)
        for i in range(len(nums)):
            next = list(range(i+1,len(nums)))
            for j in next:
                if nums[i]+nums[j] == target:
                    return [i,j]
            
                
