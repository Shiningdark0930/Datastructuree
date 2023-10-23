bgs = [int(input()) for _ in range(3)]
drs = [int(input()) for _ in range(2)]

print(min([bg + dr - 50 for bg in bgs for dr in drs]))