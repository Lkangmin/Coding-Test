answer = []
visit = []

def diff(a, b):
    temp = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            temp += 1
    return temp

def dfs(begin, target, words, cnt):
    global answer
    global visit
    if begin == target:
        answer.append(cnt)

    for i in range(len(words)):
        if diff(begin, words[i]) == 1 and visit[i] == 0:
            visit[i] = 1
            dfs(words[i], target, words, cnt+1)
            visit[i] = 0
                      

def solution(begin, target, words):
    global answer
    global visit
    visit = [0 for i in range(len(words))]
    dfs(begin, target, words, 0)
    
    if not answer:
        answer.append(0)
    return min(answer)