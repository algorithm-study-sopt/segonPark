import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
S = set()

def bfs(start, end, visit) :
    q = deque()
    q.append((start, 0))
    # set은 순서가 없고, 중복된 값을 제외하고 보여줌
    visit.add(start)

    while q :
        # start, time을 의미하는 s, t변수를 만들고 q에 처음 넣은 start, 0을 pop해서 삽입
        s, t = q.popleft()
        if s == end : return t
        t += 1

        if 0 <= s+1 <= 100000 and s+1 not in visit :
            q.append((s+1, t))
            visit.add(s+1)

        if 0 <= s - 1 <= 100000 and s-1 not in visit :
            q.append((s-1, t))
            visit.add(s-1)

        if 0 <= s*2 <= 100000 and s*2 not in visit :
            q.append((s*2, t))
            visit.add(s*2)
print(bfs(N, K, S))