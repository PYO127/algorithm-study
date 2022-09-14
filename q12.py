# p195 Q12. 주식을 사고팔기 가장 좋은 시점
from typing import List

class solution:
    def maxProfit(self, prices:List[int])->int:
        profit = 0
        min_price = 10001

        for price in prices:
            profit = max(profit, price - min_price)
            min_price = min(min_price, price)

        return profit

