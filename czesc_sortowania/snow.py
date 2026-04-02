def solve(A):
    A.sort(reverse=True)
    ans = 0
    for i in range(len(A)):
        akt = A[i]-i 
        if akt < 0:
            break
        ans += akt

    return ans 


if __name__ == "__main__":
    
    A =  [1,8,9,10,7,3,4,2,2]
    ans = solve(A)
    print(ans)