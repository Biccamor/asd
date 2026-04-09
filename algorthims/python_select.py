def get_pivot_median_of_3(arr):
    # Bierzemy pierwszy, środkowy i ostatni element
    a = arr[0]
    b = arr[len(arr) // 2]
    c = arr[-1]
    
    # Zwracamy środkową wartość z tych trzech (np. z [10, 2, 8] wróci 8)
    return sorted([a, b, c])[1] 

def quickselect_hybrid(arr, k):
    # Mądry wybór pivota bez użycia random!
    pivot = get_pivot_median_of_3(arr)
    
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    L = len(left)
    M = len(mid)
    
    if k < L:
        return quickselect_hybrid(left, k)
    elif k < L + M:
        return pivot
    else:
        return quickselect_hybrid(right, k - L - M)
    
T = [10,3,22,33,42,1,4,7,3]
ans = quickselect_hybrid(T,3)
print(T[ans], T)