#!/usr/bin/env python
# coding: utf-8

# # 스킬트리
# - 풀이 여부 : 성공
# - 아이디어
#     - skill에 있는 기술일 경우 현재 제일 먼저 배워야하는 기술(now)와 비교
#     - index 위치를 알려주는 find 함수를 이용

# In[2]:


def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        now = 0
        able = True
        for s in skill_tree:
            if s in skill:
                if skill.find(s) != now:
                    able = False
                    break
                else:
                    now += 1
        if able:
            answer += 1     
    return answer

