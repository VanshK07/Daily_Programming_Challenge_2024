def trap_rain_water(height):
    if not height:
        return 0
    
    n = len(height)
    
    max_left = [0] * n
    max_right = [0] * n
    
    max_left[0] = height[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i-1], height[i])
    
    max_right[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        max_right[i] = max(max_right[i+1], height[i])
    
    total_water = 0
    for i in range(n):
        total_water += min(max_left[i], max_right[i]) - height[i]
    
    return total_water

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap_rain_water(height)) 
