def przczepa(K,W):
    W.sort(key=lambda x: -x)
    i = 0
    ans = 0 
    while K>0:
        if W[i] <= K:
            K-=W[i]
            ans+=1
        i+=1
    print(ans, K)

K = 27
W = [2,2,8,4,1,8,16]

przczepa(K,W)