---
title: bfs dfs

---

# bfs dfs
python
# 概念
bfs是用queue來存放鄰近的節點，並將每一層的節點走完再去走下一層這樣子去走訪，而dfs則是用stack來儲存，再從上面取出，也就是說他是走到底再返回。
## 範例
如果想要走訪0 1, 0 2, 1 2, 1 3, 2 3, 2 4, 3 4, 3 5的圖形的話我們可以用bfs或dfs，那麼我們這邊先示範一下，而如我們所說的會用到queue所以要import deque，還有另外dfs會用到遞迴:
```
from collections import deque


def graph():
    n = int(input())
    e = int(input())
    graph = [[] for i in range(n)]
    for i in range(e):
        k = list(map(int, input().split()))
        graph[k[0]].append(k[1])
        graph[k[1]].append(k[0])
    return graph


def bfs(graph, s):
    dq = deque([])
    dq.append(s)
    seen = set()
    seen.add(s)

    while len(dq) > 0:
        v = dq.popleft()
        for i in graph[v]:
            if i not in seen:
                dq.append(i)
                seen.add(i)
        print(v)


bfs(graph(), 0)
```
```
def graph():
    n = int(input())
    e = int(input())
    graph = [[] for i in range(n)]
    for i in range(e):
        k = list(map(int, input().split()))
        graph[k[0]].append(k[1])
        graph[k[1]].append(k[0])
    return graph


def dfs(graph, s):
    global seen
    seen.add(s)
    print(s)
    for i in graph[s]:
        if i not in seen:
            seen.add(i)
            dfs(graph, i)


seen = set()
dfs(graph(), 0)

```
[上面的graph()是圖形的輸入](https://web.ntnu.edu.tw/~algo/Graph.html)
## 例題
[題目](https://cses.fi/problemset/task/1192/)
沒有意外的話我們用python寫應該會超時，但沒關係，我們可以試試用dfs來寫，讓他每一次遇到一個.，如果是沒有遇過的狀況下，就進行dfs搜尋:
```
import sys
sys.setrecursionlimit(10**6)
 
def inp():
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(input())
 
    return graph
 
 
def dfs(graph, v):
    global seen
    seen.add(v)
    if (
        v[0] - 1 >= 0
        and graph[v[0] - 1][v[1]] == "."
        and (v[0] - 1, v[1]) not in seen
    ):
        dfs(graph, (v[0]-1, v[1]))
 
    if (
        v[0] + 1 < len(graph)
        and graph[v[0] + 1][v[1]] == "."
        and (v[0] + 1, v[1]) not in seen
    ):
        dfs(graph, (v[0]+1, v[1]))   
 
    if (
        v[1] + 1 < len(graph[0])
        and graph[v[0]][v[1] + 1] == "."
        and (v[0], v[1] + 1) not in seen
    ):
        dfs(graph, (v[0], v[1] + 1))
 
    if (
        v[1] - 1 >= 0
        and graph[v[0]][v[1] - 1] == "."
        and (v[0], v[1] - 1) not in seen
    ):
        dfs(graph, (v[0], v[1] - 1))
 
 
def main(graph):
    global rooms
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == "." and (i, j) not in seen:
                dfs(graph, (i, j))
                rooms+=1
 
seen = set()
rooms = 0
 
main(inp())
print(rooms)

```