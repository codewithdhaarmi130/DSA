# Reverse words in a string

s = "I love Python"

words = s.split()       # split into words
words.reverse()         # reverse word order

result = " ".join(words)

print("Reversed string:", result)