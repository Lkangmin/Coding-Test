answer = 0

def dfs(numbers, target, idx, res):
    if idx == len(numbers):
        if res == target:
            global answer
            answer += 1
        return
    
    dfs(numbers, target, idx+1, res+numbers[idx])
    dfs(numbers, target, idx+1, res-numbers[idx])

def solution(numbers, target):
    global answer
    
    dfs(numbers, target, 0, 0)
    
    return answer