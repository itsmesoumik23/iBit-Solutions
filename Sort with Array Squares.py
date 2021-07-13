class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        left, right = 0, len(A) - 1
        while True:
            mid = (left + right) // 2
            if left > right:
                if mid + 1 == len(A):
                    negArray = A
                    posArray = []
                else:
                    negArray = A[:mid + 1]
                    posArray = A[mid + 1:]
                break
            if A[mid] >= 0:
                right = mid - 1
            else:
                left = mid + 1
        # print(posArray)
        # print(negArray)
        posArray = list(map(lambda x: x ** 2, posArray))
        negArray = list(map(lambda x: x ** 2, negArray))[::-1]
        print(posArray)
        print(negArray)
        arr = []
        p, q = 0, 0
        while True:
            if p == len(posArray) or q == len(negArray):
                break
            if posArray[p] < negArray[q]:
                arr.append(posArray[p])
                p += 1
            elif posArray[p] > negArray[q]:
                arr.append(negArray[q])
                q += 1
            else:
                arr.append(posArray[p])
                arr.append(negArray[q])
                p += 1
                q += 1
        while q < len(negArray):
            arr.append(negArray[q])
            q += 1

        while p < len(posArray):
            arr.append(posArray[p])
            p += 1


        return arr
