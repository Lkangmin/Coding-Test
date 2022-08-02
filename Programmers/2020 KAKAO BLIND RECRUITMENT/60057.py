def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        temp = ''
        cur = s[:i]
        cnt = 1
        
        for j in range(i, len(s), i):
            if cur == s[j:j+i]:
                cnt += 1
            else:
                if cnt > 1:
                    temp += str(cnt) + cur
                else:
                    temp += cur
                cur = s[j:j+i]
                cnt = 1
        if cnt > 1:
            temp += str(cnt) + cur
        else:
            temp += cur
        answer = min(answer, len(temp))
    return answer