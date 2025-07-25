from itertools import combinations

nums = [int(input()) for _ in range(9)]
answer = []

for comb in combinations(nums, 7):
    if sum(comb) == 100:
        #comb.sort()
        for c in comb:
            answer.append(c)
        break

answer.sort()
for c in answer:
    print(c)