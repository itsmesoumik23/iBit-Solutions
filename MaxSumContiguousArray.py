class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        sumVal = 0
        maxSoFar = -999999999999999999999999999999999
        for i in range(len(A)):
            sumVal += A[i]
            maxSoFar = max(maxSoFar, sumVal)
            if sumVal < 0:
                sumVal = 0
            
        return maxSoFar
