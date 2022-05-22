class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        temp=0
        for i in range(len(nums)):
            a=nums[i]
            if a !=0:
                nums[temp],nums[i]=nums[i],nums[temp]
                temp+=1
                
