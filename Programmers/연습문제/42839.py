from itertools import permutations

def prime(a):
    # 0.5를 1/2로 하면 시간이 늘어난다... 
    for i in range(2, int(a**0.5)+1):
        if a%i:
            continue
        else:
            return False
    return True

def solution(numbers):
    answer = 0
    total = set()
    for i in range(1, len(numbers)+1):
        total.update(set(map(int, map(''.join, permutations(numbers, i)))))

    for j in total:
        if prime(j) and j > 1:
            answer += 1
    return answer