class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for i in range(len(prices)):
            total = max([max(prices[i:]) - prices[i], total])
        
        return total