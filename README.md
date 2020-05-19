# 9012번 의문점

```
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
   ```
### 위의 코드로 했을 때 정답으로 인정됨

```
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

    if sum == 0 :
        print("YES")
    elif sum > 0 :
        print("NO")
    elif sum < 0 :
        print("NO")
   ```
   하지만 위의 경우와
   
   ```
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

    if sum == 0 :
        print("YES")
    elif sum != 0 :
        print("NO")
        ```        
위의 코드는 결과는 잘 나오지만 채점시 정답으로 인정되지 않고 틀린다..
이유가 뭘까..
    


   
