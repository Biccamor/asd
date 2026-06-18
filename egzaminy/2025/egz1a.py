# def insertion_sort(bucket):
#     """Sortowanie pomocnicze - idealne dla małych zbiorów (jak kubełki)."""
#     for i in range(1, len(bucket)):
#         key = bucket[i]
#         j = i - 1
#         while j >= 0 and bucket[j] > key:
#             bucket[j + 1] = bucket[j]
#             j -= 1
#         bucket[j + 1] = key

# def bucket_sort(arr):
#     """Główna funkcja sortowania kubełkowego."""
#     if len(arr) == 0:
#         return arr

#     n = len(arr)
#     buckets = [[] for _ in range(n)]

#     max_value = max(arr)
    
#     for num in arr:
#         index = min(n - 1, int((num / max_value) * (n - 1)))
#         buckets[index].append(num)

#     for bucket in buckets:
#         if len(bucket) > 1:
#             insertion_sort(bucket)

#     posortowana_tablica = []
#     for bucket in buckets:
#         posortowana_tablica.extend(bucket)

#     return posortowana_tablica

# def bucket_sort(arr):
#     """Główna funkcja sortowania kubełkowego."""
#     if len(arr) == 0:
#         return arr

#     n = len(arr)
#     buckets = [[] for _ in range(n)]

#     max_value = max(arr)
    
#     for num in arr:
#         index = min(n - 1, int((num / max_value) * (n - 1)))
#         buckets[index].append(num)

#     for bucket in buckets:
#         if len(bucket) > 1:
#             insertion_sort(bucket)

#     posortowana_tablica = []
#     for bucket in buckets:
#         posortowana_tablica.extend(bucket)

#     return posortowana_tablica

def battle(P,K,R):

    P.sort()
    n_k = len(K)
    n_p = len(P)
    N = max(max(K), max(P))
    T = [[0,0]]*(n_k)

    for i in range(n_k):
        T[i] = [K[i], R[i]]
    T.sort(key=lambda x: x[0])

    j = 0
    k = 0
    stos = []
    ans = 0
    for i in range(N+1):   
        if n_k > j and T[j][0] == i:
            stos.append(i+T[j][1])
            print(stos)
            j+=1
        if n_p > k and P[k] == i:
            k+=1
            while True:
                if len(stos)==0: break
                r = stos.pop()
                if i <= r:
                    ans+=1
                    break
    return ans 

P = [14, 16, 0, 6, 10, 8]
K = [2, 12, 4]
R = [8, 5, 3]
print(battle(P,K,R))