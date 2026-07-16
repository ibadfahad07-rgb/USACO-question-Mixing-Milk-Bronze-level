# Read capacity and current milk amount for each of the three buckets
cap_a, milk_a = map(int, input().split())
cap_b, milk_b = map(int, input().split())
cap_c, milk_c = map(int, input().split())

# Store capacities and milk amounts in lists, indexed 0, 1, 2
cap = [cap_a, cap_b, cap_c]
milk = [milk_a, milk_b, milk_c]

# Simulate 100 pour operations
for i in range(100):
    a = i % 3          # source bucket (cycles 0, 1, 2, 0, 1, 2, ...)
    b = (i + 1) % 3     # destination bucket (always the "next" bucket after a)
    
    space = cap[b] - milk[b]        # how much empty space is left in the destination
    amount = min(milk[a], space)    # pour as much as possible: limited by source's milk or destination's space
    
    milk[a] -= amount   # remove poured milk from source
    milk[b] += amount   # add poured milk to destination

# Print final milk amounts in each bucket, space-separated
print(*milk)