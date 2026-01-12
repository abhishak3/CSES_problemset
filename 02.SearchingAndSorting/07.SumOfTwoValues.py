def two_sum(n, target, arr):
  arr = list(zip(range(1, n+1), arr))
  arr.sort(key=lambda x : x[1])
  l, r = 0, n-1

  sm = 0
  while l < r:
    sm = arr[l][1] + arr[r][1]
    if sm == target:
      return f"{arr[l][0]} {arr[r][0]}"
    elif sm > target:
      r -= 1
    else:
      l += 1
  
  return "IMPOSSIBLE"

if __name__ == "__main__":
  n, target = map(int, input().split())
  arr = list(map(int, input().split()))

  print(two_sum(n, target, arr))