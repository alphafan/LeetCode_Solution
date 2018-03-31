"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell
the stock before you buy again).
"""

import sys


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell1 = sell2 = 0
        buy1 = buy2 = -sys.maxsize
        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1+price)
            buy2 = max(buy2, sell1-price)
            sell2 = max(sell2, price+buy2)
        return sell2
