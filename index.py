class Solution:
    def gameOfXor(self, N, A):
        x = 0

        for i in range(N):
            count = (i + 1) * (N - i)
            if count % 2 == 1:  # XOR only if the count is odd
                x ^= A[i]

        return x
