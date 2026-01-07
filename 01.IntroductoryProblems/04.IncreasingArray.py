n = int(input())
arr = list(map(int, input().split()))

ans = 0
mx = arr[0]

for i in range(1, n):
  mx = max(mx, arr[i])
  ans += mx - arr[i]

print(ans)