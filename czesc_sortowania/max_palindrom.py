def solve(s):
    i = 0
    j=1
    n = len(s)
    akt = 1
    ans = 1
    
    while i < n:

        if i+j >= n or i-j < 0:
            ans = max(ans, akt)
            akt = 1
            i+=1
            j=1
            continue

        if s[i+j]==s[i-j]:
            akt+=2
            j+=1

        else:
            ans = max(ans,akt)
            akt = 1
            i+=1
            j=1

    return ans 

ans =solve("akontnoknonabcddcba")

print(ans)