"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""

import random


class Solution(object):

    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if len(ratings) == 0:
            return 0
        givenCandy = [1]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                givenCandy.append(givenCandy[-1] + 1)
            elif ratings[i] == ratings[i - 1]:
                givenCandy.append(givenCandy[-1])
            else:
                givenCandy.append(givenCandy[-1] - 1)
        lowest = min(givenCandy)
        diff = 1 - lowest
        givenCandy = [c + diff for c in givenCandy]
        return sum(givenCandy)


s = Solution()
ratings = [random.randint(0, 10) for _ in range(1)]
numCandy = s.candy(ratings)
print(numCandy)