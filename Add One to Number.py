class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        q = len(A)-1
        while True:
            if q < 0:
                b = [1]
                b.extend(A)
                return b
            if A[q] != 9:
                A[q] += 1
                break
            else:
                A[q] = 0
                q -= 1
        for i in range(len(A)):
            if A[i] != 0:
                return A[i:]
