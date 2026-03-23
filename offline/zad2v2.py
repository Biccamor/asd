def solve(A,B):
    A.sort()
    B.sort()

    n = len(A)
    akt = 1
    ans = [1, A[0]]
    start = 1 
    end = 0
    #print(A)
    #print(B)
    while start < n:

        if A[start] <= B[end]: 
            akt +=1 
            start +=1 
        else:
            end+=1
            akt -=1 

        if ans[0] < akt:
            ans = [akt, A[start-1]]

    return ans
import sys
def get_input():
    for line in sys.stdin:
        for word in line.split():
            yield int(word)

if __name__ == "__main__":

    input_gen = get_input()
    L = []
    H =[]
    try:
        n = next(input_gen)
        t_val = next(input_gen)
        
        for _ in range(n):
            l = next(input_gen)
            h = next(input_gen)
            L.append(l)
            H.append(h)
            
        if L and H:
            ans = solve(L, H)
            print(f"{ans[0]} {ans[1]}")
        else:
            pass 

    except (StopIteration, ValueError):
        if L and H:
            ans = solve(L,H)
            print(f"{ans[0]} {ans[1]}")