

def sort_words(A, k):
    C = [0]*26
    a = ord('a')
    for el in A:
        akt = el[k]
        C[ord(akt)-a] += 1 

    for i in range(1,len(C)):
        C[i] +=  C[i-1]
    B =[None]*len(A)    
    for i in range(len(A)-1,-1,-1):
        el = A[i]
        letter = A[i][k]
        idx = C[ord(letter)-a]-1
        C[ord(letter)-a]-=1
        B[idx] = el
    
    return B


def solve(T):
    max_len = 0
    for el in T:
        max_len = max(len(el), max_len)

    buckets = [[] for _ in range(max_len+1)]
    
    for el in T:
        buckets[len(el)].append(el)
    current = []

    for akt_len in range(max_len, 0, -1): 
        current = buckets[akt_len] + current
        current = sort_words(current, akt_len-1)

    return current

if __name__ == "__main__":

    T = ["ala", "kot", "aaalaaa", "lolll", "lo", "yo", "hahahaha", "haha","hihi", "cota"]
    current = solve(T)
    print(current)