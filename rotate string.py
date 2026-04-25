# Check if one string is rotation of another

s = "abcde"
goal = "cdeab"

if len(s) == len(goal) and goal in (s + s):
    print("True")
else:
    print("False")