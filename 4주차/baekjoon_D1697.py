import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
V = set()

def BFS(start, end, visited) :
    q = deque()
    q.append((start, 0))
    visited.add(start)

    while q :
        s, c = q.popleft()
        if s == end : return c
        c += 1

        if 0 <= s + 1 <= 100000 and s + 1 not in visited :
            q.append((s + 1, c))
            visited.add(s + 1)

        if 0 <= s - 1 <= 100000 and s - 1 not in visited :
            q.append((s - 1, c))
            visited.add(s - 1)

        if 0 <= s*2 <= 100000 and s*2 not in visited :
            q.append((s*2, c))
            visited.add(s*2)

print(BFS(N, K, V))