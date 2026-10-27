class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        best = 0

        for i in range(len(prices)):
            r = len(prices) - 1
            while(i<r):
                if prices[i] <= prices[r]:
                    best = max(best, prices[r] - prices[i])
                    r = r - 1
                else:
                    r = r - 1
        return best
                        
