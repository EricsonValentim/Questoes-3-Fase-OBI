def solve():
    n = int(input())
    mod = 10**9 + 7

    if n == 0:
        print(1)
        return
    if n == 1:
        print(1)
        return
    if n == 2:
        print(5)
        return

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 5

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] * 3 + dp[i - 3] * 3) % mod

    print(dp[n])

solve()