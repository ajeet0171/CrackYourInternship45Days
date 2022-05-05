# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         for i in nums:
#             x=nums.count(i)
#             if x>1:
#                 return(i)
#                 break
#             else:
#                 continue


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
