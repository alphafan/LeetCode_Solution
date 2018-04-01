"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
"""


class Solution(object):

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        totalStations = len(gas)
        gas = gas + gas[:-1]
        cost = cost + cost
        i, length = 0, len(cost)
        start, end = 0, 0
        tank = gas[0]
        while i < length:
            if tank >= cost[i]:
                tank += (gas[i + 1] - cost[i])
                end = i + 1
            else:
                start = end = i + 1
                currGas = gas[i + 1]
            i += 1
        if end - start >= totalStations - 1:
            return start
        return -1


s = Solution()
g = [2, 1, 4]
c = [1, 2]
r = s.canCompleteCircuit(g, c)
print(r)