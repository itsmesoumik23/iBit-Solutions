class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def binarySearchRev(self, arr, left, right, val):
        if left > right:
            return -1
        mid = (left + right) // 2
        if arr[mid] < val:

            return self.binarySearchRev(arr, left, mid - 1, val)
        elif arr[mid] > val:

            return self.binarySearchRev(arr, mid + 1, right, val)
        else:
            return mid
    def binarySearch(self, arr, left, right, val):
        if left > right:
            return -1
        mid = (left + right) // 2
        if arr[mid] > val:

            return self.binarySearch(arr, left, mid - 1, val)
        elif arr[mid] < val:

            return self.binarySearch(arr, mid + 1, right, val)
        else:
            return mid

    def solve(self, A, B):
        prev = -999999999999999999
        for i in range(len(A)):
            curr = A[i]
            if curr < prev:
                end = i
                break
            prev = curr
        else:
            return -1
        # print(end, A[end])

        x = self.binarySearch(A, 0, end, B)
        y = self.binarySearchRev(A, end, len(A) - 1, B)
        if x == -1 and y != -1:
            return y
        if x != -1 and y == -1:
            return x
        else:
            return -1

