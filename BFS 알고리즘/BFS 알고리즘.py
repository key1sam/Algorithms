#!/usr/bin/env python
# coding: utf-8

# ### BFS(Breath-First-Search)
# - BFS는 너비 우선 탐색이라고도 부르며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘입니다.
# - BFS는 큐 자료구조를 이용하며, 구체적인 동작 과정은 다음과 같습니다.
#  - 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 합니다.
#  - 2. 큐에서 노드를 꺼낸 뒤, 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리합니다.
#  - 3. 더 이상 2번의 과정을 수행할 수 없을 때 까지 반복합니다.
# - 최단 거리를 구할 때 자주 사용하며 간선간의 길이가 동일할 경우 유용하게 사용한다.

# In[5]:


from collections import deque

# BFS 메서드 정의
def BFS(graph, start, visit) :
    queue = deque([start]) #덱(양쪽에서 선입선출 가능한 Queue)으로 큐를 만들기 위해 deque 라이브러리 사용)을 생성하고 
                           #deque에 start 값을 처음에 집어넣어준 것이다. 여기서 start는 1번 노드를 넣는 것이다.
    visit[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v] :
            if not visit[i] :
                queue.append(i)
                visit[i] = True
    

graph = [ [], 
          [2, 3, 8], # 1번 노드가 연결된 노드 번호들
          [1, 7], # 2번 노드
          [1, 4, 5], # 3번 노드
          [3, 5], # 4번 노드
          [3, 4], # 5번 노드
          [7], # 6번 노드
          [2, 6, 8], # 7번 노드
          [1, 7] # 8번 노드
        ] 

visit = [False] * 9 # 노드를 들렸는지 표시해줄 리스트
BFS(graph, 1, visit)    


# In[ ]:




