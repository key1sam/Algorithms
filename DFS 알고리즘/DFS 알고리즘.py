#!/usr/bin/env python
# coding: utf-8
DFS 알고리즘
 ## DFS 알고리즘
#  - 깊이 우선탐색이라고 부르며 그래프에서 깊은 부분을 우선적으로 탐색한다.
#  - 스택 혹은 재귀함수를 활용한다.
#  - 구현 과정은 다음과 같다.
#     - 탐색 시작 노드를 스택에 삽입하고 방문처리한다.
#     - 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있드만 그 노드를 스택에 넣고 방문처리
#     - 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
#     - 더 이상 방문할 노드가 없을 때까지 위 상황을 반복한다.

def DFS(graph, v, visit) : # graph 리스트를 전달해줄 때 이름을 전달해주었다.
    visit[v] = True
    print(v)
    for i in graph[v] :
        if visit[i] ==  False :
            DFS(graph, i, visit)

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
DFS(graph, 1, visit)    





