def solution(survey, choices):
    answer = ''
    total = {"R": 0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    
    for i in range(len(survey)):
        score = choices[i]-4
        if score <= 0:
            total[survey[i][0]] += abs(score) 
        else:
            total[survey[i][1]] += abs(score)
    
    answer += 'R' if total['R'] >= total['T'] else 'T'
    answer += 'C' if total['C'] >= total['F'] else 'F'
    answer += 'J' if total['J'] >= total['M'] else 'M'
    answer += 'A' if total['A'] >= total['N'] else 'N'
    
    return answer