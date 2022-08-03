from itertools import permutations

def solution(expression):
    answer = 0
    total = list(permutations(['+', '*', '-'], 3))
    arr = []
    temp = ''

    for i in expression:
        if i.isdigit():
            temp += i
            continue
        else:
            arr.append(temp)
            arr.append(i)
            temp = ''
    arr.append(temp)

    for i in total:
        arr1 = arr[:]
        for j in i:
            stack = []
            while arr1:
                k = arr1.pop(0)
                if k == j:
                    a = stack.pop()+j+arr1.pop(0)
                    stack.append(str(eval(a)))
                else:
                    stack.append(k)
            arr1 = stack
        if answer < abs(int(arr1[0])):
            answer = abs(int(arr1[0]))
        
        # 밑의 방법으로 하면 코드는 단순 but 시간 살짝 증가 (1.35ms -> 1.50ms)
        # answer = max(answer, abs(int(arr1[0])))
        
    return answer