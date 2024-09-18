from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    
    for s in strs:
        sorted_str = ''.join(sorted(s))
        anagram_map[sorted_str].append(s)
    
    return list(anagram_map.values())

strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("Grouped Anagrams:", groupAnagrams(strs1))  
