def longest_palindromic_substring(s: str) -> str:
    if len(s) == 0:
        return ""

    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest_palindrome = ""
    
    for i in range(len(s)):
        odd_palindrome = expand_around_center(i, i)
        if len(odd_palindrome) > len(longest_palindrome):
            longest_palindrome = odd_palindrome
        
        even_palindrome = expand_around_center(i, i + 1)
        if len(even_palindrome) > len(longest_palindrome):
            longest_palindrome = even_palindrome
    
    return longest_palindrome
    
s = "babad"
print(longest_palindromic_substring(s))  

s = "cbbd"
print(longest_palindromic_substring(s)) 
