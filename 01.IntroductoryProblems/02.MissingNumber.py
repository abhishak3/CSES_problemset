n = int(input())
arr = list(map(int, input().split()))

ans = 0

for num in arr:
  ans ^= num

for i in range(1, n+1):
  ans ^= i

print(ans)