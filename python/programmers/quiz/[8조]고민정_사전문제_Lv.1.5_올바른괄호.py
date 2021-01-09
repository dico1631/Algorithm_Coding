#!/usr/bin/env python
# coding: utf-8

# # 올바른괄호
# - 풀이 여부 : 성공
# - 아이디어 : stack을 이용하기

# In[2]:


def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                answer = False
                break
    if stack:
        answer = False
    return answer

