def solve(A, t):
    """przedział bez kosztow"""
    A.sort(key=lambda x: x[0])
    n = len(A)
    #dp = [0] * n 
    punkty = set()
    punkty.add(t[0])

    for i in range(0,n):
        if A[i][0] < t[0] or A[i][1] > t[1]: continue 

        if A[i][0] in punkty:
            punkty.add(A[i][1])
            if t[1] in punkty: return True 
    return t[1] in punkty


def solve_dp(A,t):
    """przedzialy z kosztami"""
    A.sort(key = lambda x: x[0])
    n = len(A)
    dp = [float('inf')]*n

    for i, (p,k,w) in enumerate(A):
        if p<t[0] or k>t[1]: continue
        
        if p==t[0]:
            dp[i] = w
            continue 

        for j in range(i):
            if A[j][1] == p:
                dp[i] = min(dp[j], dp[j] + w)

    wynik = float('inf')
    for i in range(n):
        if A[i][1] == t[1]:
            wynik = min(dp[i], wynik)
    return wynik 


def longest(A,k):

    A.sort(key= lambda x: x[0])
    n = len(A)
    dp=[[-float('inf')]*(n) for _ in range(k+1)]

    for c in range(1,k+1):
        for i in range(n):

            if c == 1:
                dp[c][i] = max(dp[c][i-1], A[i][1]-A[i][0]+1) 
                continue

            for j in range(i):
                if A[i][0] == A[j][1]:
                    if dp[c-1][j] == -float('inf'): continue
                    dp[c][i]=max(dp[c][i], dp[c-1][j] + A[i][1]-A[i][0]) 
    ans = 0
    for i in range(n):
        ans = min(ans, dp[k][i])
    return ans  



"""
dp[k][n] - tablica kxn gdzie k to ilosc krokow zwracamy maksimum 
idziemy pokolei dla kazdego mozliwej dlugosci odicnkow od 1 do k
i dla kazdej przechodzimy 

dp[1][i] = A[i][1]-A[i][0]+1 

dp[k][i] = max(dp[k][i], dp[k-1][j] + A[i][1]-A[i][0])

dla kazdego elementu przedzialu po prawej od aktualnego sprawdzamy czy da sie do niego dotrzec z obecnego
jezeli tak to sprawdzamy z wozru rekurencyjnego czy oplaca sie z poprzednim krokiem


(0,4) (4,7) (6, 10) (7, 12) (10, 14), (14, 19) (19, 21)


k = 3 

   1 2 3 4 5 6 7
1: 4 3 4 5 4 5 2  
2: 4 
3:
"""