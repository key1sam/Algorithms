#!/usr/bin/env python
# coding: utf-8

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





