class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyprice = prices[0]
        maxprofit = 0 
        for sellprice in range(1 , len(prices)):
            maxprofit = max(maxprofit , prices[sellprice] - buyprice )
            buyprice = min(buyprice , prices[sellprice] )
        return maxprofit
            
  # BestTimetoBuyandSellStock.py