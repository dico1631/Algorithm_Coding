#!/usr/bin/env python
# coding: utf-8

# # 배상비용 최소화
# - 풀이 여부 : 성공

# ## 1. 실패한 풀이
# - 아이디어 : 제곱합을 구하므로, 큰 숫자가 적을수록 값이 작아진다.
#     1. works를 오름차순 정렬
#     2. 왼쪽에서부터 n번 아래를 반복한다.<br><br>
#     3. target 값이 바로 뒤에 값보다 작아질 때까지 1씩 뺀다.
#     4. 뒤에 값보다 target 값이 작아지면 target을 오른쪽으로 1칸 이동
#     5. 3을 다시 진행
#     6. target이 제일 마지막 위치라면 0 번째 값과 비교하며, target을 옮길 땐 0 위치로 옮긴다.
#     6. 단, 값이 0이라면 빼지 않는다.
#     
# - 문제 : 바로 뒤에 값만 비교하므로 지엽적인 비교가 이루어진다.
# - 반례 : 값들이 2 이상 차이가 나는 경우 (works=[10, 7, 5, 3, 1])

# In[12]:


# 정답례
# works = [4, 3, 3]
# n = 4

# 반례
works = [10, 7, 5, 3, 1, 1]
n = sum(works)


works = sorted(works, reverse=True) 
dec = 0 

for i in range(n):
    if dec != len(works)-1: 
        if works[dec] <= works[dec+1]: dec += 1 
    else: 
        if works[dec] <= works[0]: dec = 0 
            
    if works[dec] > 0: 
        works[dec] -= 1 
    print(works)
    


print(works)
sum(map(lambda x: x**2, works))


# ## 성공한 풀이
# - 아이디어 : heap을 이용해 매번 제일 큰 값을 줄이자

# In[13]:


import heapq

def solution(n, works):
    if len(works) == 1:
        return (max(0, works[0]-n))**2
    
    
    heap = []
    leftN = min(n, sum(works))
    for work in works:
        heapq.heappush(heap, (-work, work))

    while True:
        fst = heapq.heappop(heap)[1]
        nxt = heap[0][1]
        dec = fst-nxt+1
        if dec < leftN:
            fst -= dec
            heapq.heappush(heap, (-fst, fst))
            leftN -= dec
        else:
            fst -= leftN
            heapq.heappush(heap, (-fst, fst))
            break

    return sum(map(lambda x: x[1]**2, heap))


works = [10, 7, 5, 3, 1, 1]
n = sum(works)
solution(n, works)

