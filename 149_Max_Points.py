"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""


# Condistion of 3 points p1, p2 ,p3 in a line
#
# p3.y - p2.y   p2.y - p1.y
# ----------- = -----------
# p3.x - p2.x   p2.x --p1.y
#
# Brute Force Solution:
# 1). Select two points, n(n-1)/2
# 2). Compare with all other points to see if they can align with other
# 3). Get the max points
# O(n3)
#
# Dynamic Programming ??
# From P1, P2 to get the k of y = k*x + b
# Save (P1, P2) or (P2, P1) as key to avoid deplicate computing ...
#
# Sort points first ??
#
# Divide and conc=quer ??
#

# Definition for a point.

class Point(object):

    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'


class Solution(object):

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        numPoints = len(points)
        if numPoints <= 2:
            return numPoints
        maxPointsInLine = 2
        for i in range(numPoints):
            for j in range(i + 1, numPoints):
                numPointsInLine = 2
                for k in range(j + 1, numPoints):
                    p1, p2, p3 = points[i], points[j], points[k]
                    if (p3.y - p2.y) * (p2.x - p1.x) == (p3.x - p2.x) * (p2.y - p1.y):
                        numPointsInLine += 1
                maxPointsInLine = max(maxPointsInLine, numPointsInLine)
        return maxPointsInLine


s = Solution()
a = [[0, 9], [138, 429], [115, 359], [115, 359], [-30, -102], [230, 709], [-150, -686], [-135, -613], [-60, -248],
     [-161, -481], [207, 639], [23, 79], [-230, -691], [-115, -341], [92, 289], [60, 336], [-105, -467], [135, 701],
     [-90, -394], [-184, -551], [150, 774]]
r = s.maxPoints([Point(x, y) for x, y in a])
print(r)














