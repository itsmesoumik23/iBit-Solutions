class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def cutPossible(self, arr, limit, B):
        count = 0
        for i in range(len(arr)):
            if arr[i] > limit:
                    count += (arr[i]-limit)
        if count >= B:
            return True
        return False


    def solve(self, A, B):
        start, end = 0, max(A)
        ans = -1
        while start <= end:
            mid = (start+end)//2
            if self.cutPossible(A, mid, B):
                ans = mid
                start = mid+1
            else:
                end = mid-1
        return ans
