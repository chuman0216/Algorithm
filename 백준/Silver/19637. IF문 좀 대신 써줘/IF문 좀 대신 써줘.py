import bisect

n, m = map(int, input().split())

hash = {}
sorted_list = []
for _ in range(n):
    status, strength = input().split()
    if hash.get(int(strength)):
        continue
    hash[int(strength)] = status
    sorted_list.append(int(strength))

strength_list = [int(input()) for _ in range(m)]
# sortted_hash = sorted(hash.keys())

for strength in strength_list:
    idx = bisect.bisect_left(sorted_list, strength)
    print(hash[sorted_list[idx]])
