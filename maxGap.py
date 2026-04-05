def pigeon(nums):
    n = len(nums)
    if n < 2: return 0
    
    l, h = min(nums), max(nums)
    if l == h: return 0
    
    size = max(1, (h - l) // (n - 1))

    bucket_count = (h - l) // size + 1

    min_el = [float('inf')] * bucket_count
    max_el = [float('-inf')] * bucket_count
    
    for i in range(n):
        # POPRAWKA 3: Czysty wzór matematyczny, bez '- 1' na końcu!
        idx = (nums[i] - l) // size
        
        min_el[idx] = min(nums[i], min_el[idx])
        max_el[idx] = max(nums[i], max_el[idx])
    
    prev_max = l
    ans = 0
    
    for i in range(bucket_count): # Iterujemy po bucket_count, a nie max_el
        if min_el[i] == float('inf'):
            continue
        
        akt = min_el[i] - prev_max
        ans = max(akt, ans)
        prev_max = max_el[i]
        
    return ans

if __name__=="__main__":
    nums = [1,3,100]
    ans = pigeon(nums)
    print(ans)