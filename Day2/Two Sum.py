class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a=nums[i]
            for j in range(i+1,len(nums)):
                c=nums[j]
                if a+c==target:
                    return (i,j)
        
