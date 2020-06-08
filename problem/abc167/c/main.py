n,m,x=map(int,input().split())
ans=1e9
a=[0]*n
for i in range(n):
   a[i]=list(map(int,input().split()))
for i in range(2**n):
  t=[0]*m
  cost=0
  for j in range(n):
    if (i >> j) & 1:
      cost=cost+a[j][0]
      for k in range(m):
        t[k] = t[k] + a[j][k + 1]
  if min(t) >= x:
    ans = min(ans, cost)
if ans == 1e9:
  print(-1)
else:
  print(ans)