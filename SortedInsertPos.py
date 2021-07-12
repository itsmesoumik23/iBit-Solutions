class Solution(object):
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def binarySearch(self, arr, left, right, val):

        mid = (left+right)//2
        if left == right:
            if arr[mid] > val:
                return mid
            elif arr[mid] < val:
                return mid+1
        if arr[mid] < val:
            return self.binarySearch(arr, mid+1, right, val)
        elif arr[mid] > val:
            return self.binarySearch(arr, left, mid, val)
        else:
            return mid
    def searchInsert(self, A, B):
        return self.binarySearch(A, 0, len(A)-1, B)

sol = Solution()
arr = [0, 1, 2, 3, 5, 7]
print(sol.searchInsert(arr, 4))
