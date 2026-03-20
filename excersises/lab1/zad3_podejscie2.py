def solve(A,x):
    i = 0
    j = len(A)-1

    while i<=j: 
        if A[i] + A[j] == x:
            return True
        elif A[i]+A[j]>x:
            j-=1
        else:
            i+=1

    return False


if __name__ == "__main__":
    A = [1,4,6,7,8,10,13,15,20,24]
    ans = solve(A,23)
    print(ans)