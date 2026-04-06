# Merge intervals

intervals = [[1,3], [2,6], [8,10], [15,18]]

# Step 1: Sort intervals
intervals.sort()

merged = []

for interval in intervals:
    # If list is empty or no overlap
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        # Merge intervals
        merged[-1][1] = max(merged[-1][1], interval[1])

print("Merged intervals:", merged)