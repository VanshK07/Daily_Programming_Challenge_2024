def permute_unique(s):
    def backtrack(path, used):
        if len(path) == len(s):
            result.append(''.join(path))
            return
        
        for i in range(len(s)):
            if used[i] or (i > 0 and s[i] == s[i-1] and not used[i-1]):
                continue
            
            used[i] = True
            path.append(s[i])
            
            backtrack(path, used)
            
            path.pop()
            used[i] = False

    s = sorted(s)
    result = []
    used = [False] * len(s)
    backtrack([], used)
    
    return result

input_string = "abc"
print(permute_unique(input_string))
