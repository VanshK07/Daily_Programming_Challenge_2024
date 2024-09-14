def find_zero_sum_subarrays(arr):
    prefix_map = {}
    result = []
    prefix_sum = 0
    
    for i in range(len(arr)):
        prefix_sum += arr[i]
        
        if prefix_sum == 0:
            result.append((0, i))
       
        if prefix_sum in prefix_map:
            for start_index in prefix_map[prefix_sum]:
                result.append((start_index + 1, i))
        
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = []
        prefix_map[prefix_sum].append(i)
    
    return result

arr = [3, 4, -7, 1, 3, 3, 1, -4, -2, 2]
subarrays = find_zero_sum_subarrays(arr)
print("Subarrays with zero sum are:", subarrays)
