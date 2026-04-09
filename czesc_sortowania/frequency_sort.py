def counting(A):
    B = [0]*(max(A)+1)

    for i in A:
        B[i] += 1


    #for i in range(1, len(B)):
    #    B[i] += B[i-1] 

    C =[0]*(max(B)+1)

    for i in B:
        C[i] += 1
    
    for i in range(len(C)-2,-1,-1):
        C[i] += C[i+1]
    ans =[0]*len(A)
    print(A)
    print(B) # ile razy sie pojawia dana liczba 
    print(C) # na ktorej pozycji dane liczby

    for i in range(0, len(A)):    
        #C[B[i]] -= 1x
        #ans[C[B[i]]] = A[i]
        C[B[A[i]]]-=1
        ans[C[B[A[i]]]] = A[i]
    
    print(ans)

def solve(A):
    counting(A)


if __name__ == "__main__":
    A = [10,2,3,3,5,3,4,10,2,3,3,7,9,7,7,8,1,3]
    counting(A)