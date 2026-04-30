# Longest Palindromic Substring

s = "babad"

start = 0
max_len = 1

def expand(left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

for i in range(len(s)):
    len1 = expand(i, i)       # odd length
    len2 = expand(i, i + 1)   # even length
    max_length = max(len1, len2)

    if max_length > max_len:
        max_len = max_length
        start = i - (max_length - 1) // 2

print("Longest palindrome:", s[start:start + max_len])