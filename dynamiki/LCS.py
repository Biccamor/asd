def solve(A:list,B:list):
    dp = [[0]*len(B) for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[len(A)-1][len(B)-1]


if __name__ == "__main__":
    A = ['B', 'A', 'J', 'T', 'E', 'K']

    B = ['A', 'N', 'A', 'L', 'I', 'T', 'Y', 'K']

    print(solve(A,B))