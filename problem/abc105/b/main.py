n = int(input())
cmax = 100 // 4
dmax = 100 // 7
for i in range(0, cmax + 1):
    for j in range(0, dmax + 1):
        if i * 4 + j * 7 == n:
            print("Yes")
            exit()
print("No")