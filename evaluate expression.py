class Solution:
	# @param A : list of strings
	# @return an integer
    
    #precedance
    # "/", "*", "+", "-"
	def evalRPN(self, A):
        stack = []
        for i in range(len(A)):
            if A[i] in ["/", "*", "+", "-"]:
                second = int(stack.pop())
                first = int(stack.pop())
                if A[i] == "/":
                    res = first // second
                if A[i] == "*":
                    res = first * second
                if A[i] == "+":
                    res = first + second
                if A[i] == "-":
                    res = first - second
                stack.append(res)
            else:
                stack.append(A[i])
        return stack[-1]
