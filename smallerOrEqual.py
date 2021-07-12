class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        left, right = 0, len(A)-1
        idx = -1
        while left <= right:
            mid = (left+right)//2
            count = left
            if A[mid] <= B:
                idx = mid
                left = mid+1
            elif A[mid] > B:
                right = mid-1

        return idx+1
