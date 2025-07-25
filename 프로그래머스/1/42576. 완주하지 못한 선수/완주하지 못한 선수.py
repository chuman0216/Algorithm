from collections import Counter

def solution(participant, completion):
    
    comp_hash = Counter(completion)
    part_hash = Counter(participant)
    
    for i in participant:
        if comp_hash.get(i) == None or comp_hash.get(i) != part_hash.get(i):
            return i