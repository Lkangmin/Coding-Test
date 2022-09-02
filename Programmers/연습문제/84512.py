from itertools import product

def solution(word):
    answer = 0
    base = ['A', 'E', 'I', 'O', 'U']
    
    total = []
    for i in range(1, 6):
        total.extend(list(map(''.join,product(base, repeat=i))))
    
    total.sort()
    
    answer = total.index(word) + 1
    return answer