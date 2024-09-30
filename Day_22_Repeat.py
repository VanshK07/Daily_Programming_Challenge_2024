def first_element_to_repeat_k_times(arr, k):
    count = {}
    
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
        
        if count[num] == k:
            return num
    
    return -1
arr = [1, 2, 3, 2, 4, 3, 2]
k = 2
print(first_element_to_repeat_k_times(arr, k)) 
