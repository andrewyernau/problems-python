#You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

#You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

#Return the maximum profit you can achieve. You may choose to not make any transactions, 
# in which case the profit would be 0.

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        bestSell = 0
        minP = float('inf') # Arbitrary number
        for profit in prices:
            minP = min(minP,profit)
            bestSell = max(bestSell, profit - minP)
        
        return bestSell
        
prices = [10,1,5,6,7,1]
solution = Solution()
output = solution.maxProfit(prices)
print(f"Input: {prices}")
print(f"Output: {output}") # Output: 6

prices=[7,6,4,3,1]
solution = Solution()
output = solution.maxProfit(prices)
print(f"Input: {prices}")
print(f"Output: {output}") # Output: 0