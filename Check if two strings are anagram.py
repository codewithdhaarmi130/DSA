# Check if two strings are anagram

s = "anagram"
t = "nagaram"

if len(s) != len(t):
    print("False")
else:
    freq = {}

    # Count characters in s
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Subtract using t
    for ch in t:
        if ch not in freq or freq[ch] == 0:
            print("False")
            break
        freq[ch] -= 1
    else:
        print("True")