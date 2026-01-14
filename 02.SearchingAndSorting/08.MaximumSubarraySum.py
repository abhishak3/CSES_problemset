def max_subarray_sum(n, arr):
  sm = 0
  ans = arr[0]

  for num in arr:
    sm += num
    ans = max(ans, sm)

    if sm < 0:
      sm = 0
  
  return ans

if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))
  print(max_subarray_sum(n, arr))