def solve(S,B,L):
    akt_L = L
    ans = 0
    for i in range(1,len(S)):
        
        if S[i]-S[i-1]>L:
            return -1

        if S[i]-S[i-1] > akt_L:
            akt_L = L - S[i] -S[i-1]
            ans +=1
        else:
            akt_L = S[i]-S[i-1]
        if S[i] == B: return ans 
    
    return ans 


def solve_2(S,B,L):
   
    cost = 0 
    akt_L = L
    akt = S[0][0]
    i = 0 
    while akt != B: 
        for j in range(i, len(S)):
            if S[j][0] - S[i][0] > L: 
                break 
        
            if S[j][1] < S[i][1]: 
                if akt_L - S[]
    