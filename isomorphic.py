# Check if two strings are isomorphic

s1 = "earth"
s2 = "add"

map1 = {}
map2 = {}

is_isomorphic = True

for c1, c2 in zip(s1, s2):
    if (c1 in map1 and map1[c1] != c2) or (c2 in map2 and map2[c2] != c1):
        is_isomorphic = False
        break
    map1[c1] = c2
    map2[c2] = c1

if is_isomorphic:
    print("Isomorphic")
else:
    print("Not Isomorphic")