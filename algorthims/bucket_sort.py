def insertion_sort(bucket):
    """Sortowanie pomocnicze - idealne dla małych zbiorów (jak kubełki)."""
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(arr):
    """Główna funkcja sortowania kubełkowego."""
    if len(arr) == 0:
        return arr

    n = len(arr)
    buckets = [[] for _ in range(n)]

    max_value = max(arr)
    
    for num in arr:
        index = min(n - 1, int((num / max_value) * (n - 1)))
        buckets[index].append(num)

    for bucket in buckets:
        if len(bucket) > 1:
            insertion_sort(bucket)

    posortowana_tablica = []
    for bucket in buckets:
        posortowana_tablica.extend(bucket)

    return posortowana_tablica

# --- Przykład użycia ---
if __name__ == "__main__":
    test_arr = [42, 32, 33, 52, 37, 47, 51]
    print("Przed:", test_arr)
    print("Po:  ", bucket_sort(test_arr))