def radix_sort(A, max_len):

    for i in range(max_len-1, -1, -1):
        A = counting_sort(A,i)
    return A
    

def counting_sort(B, pos):
    alf = [0]*27
    a = ord('a')
    for el in B:
        litera = el[pos]
        if litera == " ": 
            alf[0]+=1
            continue
        alf[ord(litera) - a +1] += 1

    C = [0]*27
    C[0] = alf[0]
    for i in range(1, len(alf)):
        C[i] = alf[i] + C[i-1]

    ANS = [0]*(len(B))
    for i in range(len(B)-1, -1, -1):
        akt = B[i][pos]
        if akt == " ":
            C[0] -= 1
            ANS[C[0]] = B[i]
            continue
        C[ord(B[i][pos])-a+1] -= 1
        ANS[C[ord(B[i][pos])-a+1]] = B[i]
    return ANS


def solve(T):
    
    A = []
    max_len = 0
    for el in T:
        max_len = max(len(el), max_len)

    
    for el in T:
        
        reverse = el[::-1]
        el = min(el, reverse)
        akt_len = len(el)
        el += " "*(max_len-akt_len)

        A.append(el)

    A = radix_sort(A, max_len)

    prev = A[0]
    ans = 1
    akt = 1
    
    for el in A[1:]:
        if el != prev:
            ans = max(akt, ans)
            akt = 1
        else:
            akt+=1
        prev = el 

    return max(ans, akt)

if __name__ == "__main__":
    B = ["pies", "mysz", "kot", "tok", "kogut", "seip", "siep", "pies"]
    print(solve(B))