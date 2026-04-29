# Sort characters by frequency

s = "tree"

freq = {}

# Count frequency
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

# Sort by frequency (descending)
sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# Build result
result = ""

for ch, count in sorted_chars:
    result += ch * count

print("Sorted string:", result)