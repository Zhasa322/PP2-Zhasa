N, K = input().split()
N = int(N)
K = int(K)

kegels = ["I"] * N

for a in range(K):
    li, ri = input().split()
    li = int(li)
    ri = int(ri)
    for j in range(li - 1, ri):
        kegels[j] = "." 
print("".join(kegels))

