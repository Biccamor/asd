def change(amount: int, coins):
    dp = [0]*(amount+1)
    dp[0]=1
    for c in coins:
        for i in range(0, amount+1):
            if dp[i] == 0: continue

            if i + c > amount: continue
            dp[i+c] += dp[i]

    print(dp[amount])


amount = 5
coins = [1,2,5]
change(amount, coins)