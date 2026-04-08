def counting(A,B,word,a):
    for el in word:
        A[ord('el')-a] += 1
    B[0] = A[0]
    for i in range(1,len(A)):
        B[i] = A[i] + B[i-1]
        

def solve(T):
    a = ord('a')
    A = [0]*26
    B = [0]*26
    for word in T:
        ...