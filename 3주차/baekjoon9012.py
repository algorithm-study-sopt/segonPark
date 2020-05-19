import sys

T = int(sys.stdin.readline())
for i in range(T) :
    V = list(sys.stdin.readline())
    sum = 0
    for j in V :
        if j == "(" :
            sum += 1
        elif j == ")" :
            sum -= 1

        if sum < 0 :
            print("NO")
            break

    if sum == 0 :
        print("YES")
    elif sum > 0 :
        print("NO")

