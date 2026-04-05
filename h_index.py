def counting_sort(nums):
    A = [0]*(max(nums)+1)

    for el in nums:
        A[el] += 1

    B = [0]*(max(nums)+1)

    B[0] = A[0]
    for i in range(1,len(A)): 
        B[i] = B[i-1] + A[i]
    
    C = [0]*len(nums)

    for i in range(len(nums)-1, -1, -1):
        
        B[nums[i]]-=1
        C[B[nums[i]]] = nums[i] 
    return C

def solve(nums):
    nums = counting_sort(nums)

    h_idx = 0

    for i in range(len(nums)-1, -1, -1):

        if nums[i] >= h_idx+1:
            h_idx += 1
        else:
            break
    return h_idx

if __name__ == "__main__":
    nums = [3,0,6,1,5]
    ans = solve(nums)
    print(ans)
