size = int(input())
A = [int(i) for i in input().split()]


element, index = map(int,input().split())
for h in range(len(A)+1):
    if h == index:
        B = A[:index - 1] + [element] + A[index-1:]

for k in range(len(B)):
    print(B[k], end=" ")
