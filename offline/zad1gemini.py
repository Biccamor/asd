import sys
from random import randint, seed


OIOIOI = True

sys.setrecursionlimit(200000)
def merge(A, B, dom, p, q, r): 
    i = p 
    j = q
    k = p

    while i < q and j < r:
        if A[i][1] < A[j][1]:
            B[k] = A[i]
            i += 1
        else:
            dom[A[j][0]] += i - p
            B[k] = A[j]
            j += 1
        k += 1

    if i < q:
        B[k:r] = A[i:q]
    else:

        B[k:r] = A[j:r]
        for idx in range(j, r):
            dom[A[idx][0]] += q - p

    A[p:r] = B[p:r]


def merge_sort(A, B, dom, p, r):
    if r - p <= 1: 
        return 

    q = (p + r) // 2
    merge_sort(A, B, dom, p, q)
    merge_sort(A, B, dom, q, r)
    merge(A, B, dom, p, q, r)


def solution(T):
    if not T: return 0
    T[:] = [(i, val) for i, val in enumerate(T)]

    n = len(T)
    B = [0] * n
    dom = [0] * n
    
    merge_sort(T, B, dom, 0, n)
    
    return max(dom)

if __name__ == "__main__":
    def generate_random_string(length):
        return ''.join(chr(randint(97, 122)) for _ in range(length))
    
    if OIOIOI:
        n = int(sys.stdin.readline().strip())
        words = [sys.stdin.readline().strip() for _ in range(n)]
        print(solution(words))
    else:
        seed(1)
        test_def = [
            (10, 5, 10, 6),
            (100, 5, 10, 88),
            (100, 20, 100, 91),
            (10000, 10, 30, 9901)
        ]
        ok = 0
        for idx, (n, m_low, m_high, ans) in enumerate(test_def):
            print("Test", idx + 1)
            words = [generate_random_string(randint(m_low, m_high)) for _ in range(n)]
            result = solution(words)
            if result == ans:
                print("OK")
                ok += 1
            else:
                print("Błąd!")
        print("Wynik:", ok, "/", len(test_def))