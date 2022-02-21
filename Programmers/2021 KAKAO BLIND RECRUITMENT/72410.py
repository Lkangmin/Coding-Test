#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

def solution(new_id):
    # 1
    answer = new_id.lower()
    
    # 2
    answer = ''.join(re.findall('[a-z0-9-_.]',answer))
    
    # 3
    while '..' in answer:
        answer = answer.replace('..','.')
    
    # 4
    answer = answer.strip('.')
    
    # 5
    if not answer:
        answer += 'a'
    
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        answer = answer.strip('.')
    
    # 7
    if len(answer) < 3:
        while len(answer) < 3:
            answer += answer[-1]
    
    return answer

