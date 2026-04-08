def partition(T,n,l,r):
    pivot = T[r-1]
    i = l-1
    for j in range(l,r):
        if T[j] < pivot: 
            i+=1
            T[j],T[i]= T[i], T[j]
    T[r-1],T[i+1]=T[i+1],T[r-1]
    return i+1

def quickselect(T,k,l,r):
    n = len(T)
    
    while l<=r:
        idx = partition(T,n, l, r)
        
        if idx == k:
            return idx
        
        elif idx<k:
            l = idx + 1 
        else:
            r = idx-1
    return l



def solve(T): 
    n = len(T)
    ans = [[0]*n for _ in range(n)]
    
    flatT =[]
    for i in range(n):
        for j in range(n):
            flatT.append(T[i][j])
    
    min_adj = (n*(n-1))//2+1
    max_adj = min_adj+n

    min = flatT[quickselect(flatT,min_adj,0,n*n)]
    maxi = flatT[quickselect(flatT,max_adj,0,n*n)]
    start = 1
    mid = 0
    end = max_adj+1 

    for el in flatT:
        if el < min:
            block = start // n
            idx = start - block*n
            ans[block][idx] = el 
        elif el > min and el < maxi: 



if __name__ == "__main__":
    T = [[2, 3 ,5], [7, 11, 13 ], [17,19,23 ]]
    solve(T)