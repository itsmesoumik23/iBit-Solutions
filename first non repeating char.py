
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        prev = dict()
        block = dict()
        queue = []
        qSize = 0
        front = 0
        res = ""
        for i in range(len(A)):
            if A[i] not in prev:
                prev[A[i]] = True
                queue.append(A[i])
                qSize += 1
            else:
                block[A[i]] = True
                while front < qSize and queue[front] in block:
                    front += 1
            if front != qSize:
                res += queue[front]
            else:
                res += "#"
        return res


