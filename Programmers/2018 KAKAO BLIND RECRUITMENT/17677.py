import re
from collections import Counter

def solution(str1, str2):
    answer = 1
    
    set1 = Counter([(str1[i]+str1[i+1]).lower() for i in range(len(str1)-1) if (str1[i]+str1[i+1]).isalpha()])
    set2 = Counter([(str2[i]+str2[i+1]).lower() for i in range(len(str2)-1) if (str2[i]+str2[i+1]).isalpha()])

    a_len = len(list((set1&set2).elements()))
    b_len = len(list((set1|set2).elements()))
    
    if a_len > 0 and b_len > 0:
        answer = a_len/b_len
    elif b_len > 0:
        answer = a_len/b_len

    answer = int(answer*65536)
    
    return answer