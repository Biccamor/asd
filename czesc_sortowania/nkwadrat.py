def count_sort(t,n,d):
    C = [0]*n

    for i in t:
        idx = (i//d) % n
        C[idx] += 1 

    for i in range(1,len(C)):
        C[i] += C[i-1]
    
    ans = [0]*n

    for i in range(len(C)-1, -1,-1):
        idx = (t[i] // d) %n
        C[idx] -= 1
        ans[C[idx]] = t[i]    

    for i in range(len(ans)):
        t[i] = ans[i]


def solve(tab):
    n = len(tab)

    count_sort(tab,n,1)
    count_sort(tab,n,n)
    count_sort(tab,n,n*n)
    print(tab)


if __name__ == "__main__": 

    tab = [4,294,44,100,163,16,28]
    solve(tab)