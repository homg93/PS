import sys
 
def solve(dp, n, cost) :
    for i in range(n) :
        if i == 0 :
            dp[i][0] = cost[i][0]
            dp[i][1] = cost[i][1]
            dp[i][2] = cost[i][2]
            continue
        # R
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        # G
        dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
        # B
        dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])
 
    min_val = min(dp[n-1][0], dp[n-1][1])
    min_val = min(min_val, dp[n-1][2])
    return min_val
 
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    cost = []
    for _ in range(n) :
        temp = list(map(int, sys.stdin.readline().split()))
        cost.append(temp)
    dp = [[-1]*3 for _ in range(n)]
    print(solve(dp, n, cost))