class Solution:
    def sortColors(self, nums: List[int]) -> None:
        lo,mid,hi=0,0,len(nums)-1
        while(mid<=hi):
            if nums[mid]==0:
                nums[mid],nums[lo]=nums[lo],nums[mid]
                mid+=1
                lo+=1
            elif nums[mid]==2:
                nums[mid],nums[hi]=nums[hi],nums[mid]
                # mid+=1
                hi-=1
            else:
                mid+=1
