from itertools import combinations
from collections import defaultdict
import bisect

def solution(info, query):
    answer = []
    total_info = defaultdict(list)
    for i in info:
        temp = i.split()
        value = int(temp.pop())
        for j in range(len(temp)+1):
            for k in combinations(temp, j):
                total_info[k].append(value)
        
    # info의 최대 길이 50000 / query는 100000 -> 미리 sort 하는게 더 효율적 
    for i in total_info.keys():
        total_info[i].sort()
    
    for i in query:
        q = i.split(' and ')
        q.extend(q.pop().split())
        value = int(q.pop())
        temp = [i for i in q if i != '-']
        scores = total_info[tuple(temp)]
        answer.append(len(scores) - bisect.bisect_left(scores, value))

    return answer