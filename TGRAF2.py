def LMIS(arr):
    n = len(arr)
    dp = [[] for _ in range(n)]

    for i in range(n):
        dp[i] = [arr[i]]
        for j in range(i):
            if arr[j] < arr[i] and len(dp[j]) + 1 > len(dp[i]):
                dp[i] = dp[j] + [arr[i]]

    return max(dp, key=len)

arr = [4,1,13,7,0,2,8,11,3]
print(LMIS(arr))
