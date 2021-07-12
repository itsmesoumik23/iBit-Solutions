from math import floor
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, x):
        left, right = 0, x
        mid = -1
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 > x:
                right = mid - 1
            elif mid ** 2 < x:
                left = mid + 1
            else:
                return mid
        return mid if mid**2 < x else mid-1
