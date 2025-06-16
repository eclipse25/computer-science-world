## DFS (깊이 우선 탐색, Depth-First Search)

<img src="../_assets/bfs-dfs.gif" width="500" />

<br>

- 그래프의 모든 노드를 방문하기 위한 알고리즘
- 루트 노드(혹은 다른 임의의 노드)에서 시작해, 다음 분기(branch)로 넘어가기 전에 해당 분기를 최대한 **깊게** 탐색한다.
- 스택(Stack)을 사용하거나 재귀적 방법을 통해 구현한다.
- 재귀적 방법을 통해 DFS를 사용할 경우, 파이썬에서는 재귀 호출의 깊이가 제한되어 있으므로 필요한 경우 `sys.setrecursionlimit()`을 사용하여 이 제한을 늘릴 수 있다.

- 모든 케이스 중 가지치기를 하며 탐색하는 백트래킹(Backtracking)이 DFS를 기반으로 한다.
    - 일반적인 대부분의 그래프 문제들은 BFS로도 풀리지만, 백트래킹의 경우 DFS를 사용해야 한다.
    - N-Queen 문제가 대표적인 예시이다.

<br>

### DFS 알고리즘의 기본 절차

1. 노드 방문
    - 시작 노드를 방문하고, 방문한 노드를 스택에 푸시(push)하며 방문 처리를 한다.

2. 인접 노드 탐색
    - 현재 노드에 인접한 노드 중에서 방문하지 않은 노드를 하나 선택하고, 그 노드를 방문한다. 
    - 방문한 노드를 스택에 푸시하고 방문 처리 한다.

3. 더 이상 탐색할 노드가 없을 때까지 반복
    - 현재 노드에 방문하지 않은 인접 노드가 더 이상 없다면, 스택에서 최상위 노드를 팝(pop)하여 빼내고, 그 노드를 현재 노드로 설정한다. 이 과정을 스택이 비워질 때까지 반복한다.

4. 모든 노드 방문
    - 스택이 비워지면 탐색을 종료한다.

<br>

### DFS 알고리즘 구현 예시 - 재귀 (Python)

다음 코드는 그래프에서 'A' 노드부터 시작하여 DFS 방식으로 모든 노드를 탐색하고, 방문한 노드를 출력한다.  
visited 집합은 방문한 노드를 기록하여, 이미 방문한 노드를 다시 방문하지 않도록 한다.  
인접한 모든 노드가 visited여서 더이상 방문할 노드가 없으면 재귀가 종료된다.  

```python
# DFS 알고리즘 구현 (재귀적 방식)
def dfs(graph, node, visited):
    # 현재 노드를 방문 처리
    visited.add(node)
    print(node, end=' ')

    # 현재 노드의 인접 노드를 확인하고, 방문하지 않은 노드를 DFS로 재귀적으로 방문
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# 간단한 그래프 예시
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 방문한 노드를 저장할 집합
visited = set()

# 'A'에서 시작하는 DFS 실행
dfs(graph, 'A', visited)

```

<br>

### DFS 알고리즘 구현 예시 - Stack (Python)

```python
def dfs_with_stack(graph, start_node):
    # 방문한 노드를 저장할 집합
    visited = set()
    # DFS를 위한 스택, 시작 노드를 포함하여 초기화
    stack = [start_node]

    # 스택이 비어있지 않는 동안 반복
    while stack:
        # 스택에서 하나의 노드를 꺼냄
        node = stack.pop()
        # 현재 노드를 방문하지 않았다면
        if node not in visited:
            # 방문 처리
            visited.add(node)
            print(node, end=' ')

            # 현재 노드에 인접한 노드 중 방문하지 않은 노드들을 스택에 추가
            # 여기서는 인접 노드를 거꾸로 스택에 추가하여, 그래프의 자연스러운 순서대로 방문하게 함
            stack.extend([x for x in graph[node] if x not in visited])

# 간단한 그래프 예시
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 'A'에서 시작하는 DFS 실행
dfs_with_stack(graph, 'A')

```