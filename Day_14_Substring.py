def count_substrings_with_k_distinct(s, k):
    def count_at_most_k_distinct(s, k):
        count = 0
        left = 0
        char_freq = {}
        
        for right in range(len(s)):
            if s[right] not in char_freq:
                char_freq[s[right]] = 0
            char_freq[s[right]] += 1
    
            while len(char_freq) > k:
                char_freq[s[left]] -= 1
                if char_freq[s[left]] == 0:
                    del char_freq[s[left]]
                left += 1
            count += right - left + 1
        
        return count
    return count_at_most_k_distinct(s, k) - count_at_most_k_distinct(s, k-1)
s = "pqpqs"
k = 2
print(count_substrings_with_k_distinct(s, k)) 
