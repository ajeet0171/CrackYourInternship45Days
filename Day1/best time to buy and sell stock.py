# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         # prices = [7,1,5,3,6,4]
#         arr=[]
#         for i in range(len(prices)):
#             a=prices[i]
#             for j in range(i+1,len(prices)):
#                 b=prices[j]
#                 if b>a:
#                     arr.append(b-a)
#         arr.sort()
#         c=len(arr)
#         if c==0:
#             return("0")
#         else:
#             return(arr[len(arr)-1])
#                 time limit exceeded
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPurchase = prices[0]
        for i in range(1, len(prices)):		
            maxProfit = max(maxProfit, prices[i] - minPurchase)
            minPurchase = min(minPurchase, prices[i])
        return maxProfit
