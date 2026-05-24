def tab(X):
    X.sort()

    interval = [X[0], X[0]+1]
    ans = 1
    for i in range(1, len(X)):
        if X[i] <= interval[1]: 
            continue
        
        interval = [X[i], X[i]+1]
        ans += 1 
    return ans

X = [0.4, 1.3, 2.4, 3.4, 7.0]

print(tab(X))