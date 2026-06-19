def candy(ratings) -> int:
    ans = len(ratings)
    n = len(ratings)
    candies = [1]*n
    for i in range(1,n):
        if ratings[i] < ratings[i-1]:
            #if candie[i-]
            candies[i-1] += 1
            ans+=1
    for i in range(n-2, -1, -1):
        if ratings[i+1] > ratings[i]:
            if candies[i+1] <= candies[i]:
                ans = ans + candies[i+1]-candies[i]+1
                candies[i+1] = candies[i]+1
    return ans  

ratings = [1,2,2]
ratings2 = [1,3,2,2,1]

candy(ratings)