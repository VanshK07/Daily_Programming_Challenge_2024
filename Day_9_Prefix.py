def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    
    for s in strs[1:]:
        while s[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

strs1 = ["flower", "flow", "flight"]
print("Longest Common Prefix:", longestCommonPrefix(strs1)) 

strs2 = ["dog", "racecar", "car"]
print("Longest Common Prefix:", longestCommonPrefix(strs2))  

