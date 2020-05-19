import sys

N, K = map(int, sys.stdin.readline().split())
Original = [i for i in range(1, N+1)]
result = list()
gap = K - 1

for i in range(N) :
    if len(Original) > gap :
        result.append(Original.pop(gap))
        gap += K - 1

    elif len(Original) <= gap :
        gap = gap % len(Original)
        result.append(Original.pop(gap))
        gap += K - 1

print("<", end = '') # end에 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 나옴
for i in result :
    if i == result[-1] : print(i, end = "")
    else : print("%d,"%(i), end = ' ') # end에 공백을 한 칸 지정하며 다음 번 출력이 한 칸 띄어져서 나옴
print(">")

