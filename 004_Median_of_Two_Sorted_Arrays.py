"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #       Left-Part         |     Right-Part
        # A[0], A[1], ..., A[i-1] | A[i], A[i+1], ..., A[-1] ----> length m
        # B[0], B[1], ..., B[j-1] | B[j], B[j+1], ..., B[-1] ----> length n
        # i + j =  m - i + n - j (or m -i + n - j +1)
        # 2j = m+n-2i (+1) --> j = int((m+n+1)/2) +i
        # max(A[i-1], B[j-1]) <= min(A[i], B[j])
        # if m < n
        # i : 0 .. m-1
        # j : int((m+n+1)/2) - i
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        imin, imax, halflen = 0, m, (m+n+1)/2
        while imin <= imax:
            i = int((imin+imax)/2)
            j = halflen - i
            if i < m and nums1[i] < nums2[j-1]:
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])

                if (m+n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return float((max_of_left+min_of_right)/2)

