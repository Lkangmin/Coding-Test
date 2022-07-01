def solution(id_list, report, k):
    answer = []
    new_report = {}
    report = list(set(report))
    for i in report:
        temp = i.split()
        if new_report.get(temp[0]):
            new_report[temp[0]].append(temp[1])
        else:
            new_report[temp[0]] = [temp[1]]

    # 유저 신고 횟수 계산
    report_cnt = {}
    for i in sum(new_report.values(), []):
        if report_cnt.get(i):
            report_cnt[i] += 1
        else:
            report_cnt[i] = 1
    
    # 메일 횟수 계산
    for i in id_list:
        cnt = 0
        if new_report.get(i):
            for j in new_report[i]:
                if report_cnt[j] >= k:
                    cnt += 1
        answer.append(cnt)

    return answer