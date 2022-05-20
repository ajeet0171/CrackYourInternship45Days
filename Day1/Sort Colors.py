# dutch national flag algorithm
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
# method 2 using count sort
# count sort    
def sortColors1(self, nums):
    c0 = c1 = c2 = 0
    for num in nums:
        if num == 0:
            c0 += 1
        elif num == 1:
            c1 += 1
        else:
            c2 += 1
    nums[:c0] = [0] * c0
    nums[c0:c0+c1] = [1] * c1
    nums[c0+c1:] = [2] * c2
