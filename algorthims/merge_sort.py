def mergeSort(array:list[int]) -> list[int]:

    if len(array) <= 1: return array
    mid = len(array)//2

    left_arr = array[:mid]
    right_arr = array[mid:]

    mergeSort(left_arr)
    mergeSort(right_arr)
    array = merge(left_arr, right_arr, array)

def merge(left_arr: list[int], right_arr: list[int], array: list[int]) -> list[int]:

    l, r, i = 0, 0,0
    r_max = len(right_arr)
    l_max = len(left_arr)

    while l<l_max and r<r_max:

        if left_arr[l] < right_arr[r]:
            array[i] = left_arr[l]
            l+=1 
            i+=1

        else:
            array[i] = right_arr[r]
            r+=1
            i+=1

    while l<l_max:
        array[i] = left_arr[l]
        l+=1
        i+=1
    
    while r<r_max:
        array[i] = right_arr[r]
        r+=1
        i+=1
    
    return array


if __name__=="__main__":
    arr = [10,2,4,43,5,2,17,234]
    mergeSort(arr)
    print(arr)