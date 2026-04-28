# Implement ATOI

s = "   -42abc"

s = s.strip()   # remove spaces
if not s:
    print(0)
else:
    sign = 1
    i = 0
    result = 0

    # Check sign
    if s[0] == '-':
        sign = -1
        i += 1
    elif s[0] == '+':
        i += 1

    # Convert digits
    while i < len(s) and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1

    result *= sign

    # Handle overflow
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1

    if result < INT_MIN:
        result = INT_MIN
    if result > INT_MAX:
        result = INT_MAX

    print("Integer value:", result)