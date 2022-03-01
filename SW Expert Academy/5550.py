T = int(input())

for test_case in range(1, T + 1):
    sound = input()
    max_frog = 0
    cnt = {'c':0, 'r':0, 'o':0, 'a':0, 'k':0}

    for i in sound:
        cnt[i] += 1
        # croak 순서를 지키지 않으면 잘못된 소리이다.
        if cnt['c'] >= cnt['r'] >= cnt['o'] >= cnt['a'] >= cnt['k']:
            # 현재 겹쳐지는 개구리 울음소리 갱신
            max_frog = max(max(cnt.values()), max_frog)
            if i=='k':
                for k in cnt.keys():
                    cnt[k]-=1
        else:
            break

    if max(cnt.values()):
        print('#{} {}'.format(test_case, -1))
    else:
        print('#{} {}'.format(test_case, max_frog))
