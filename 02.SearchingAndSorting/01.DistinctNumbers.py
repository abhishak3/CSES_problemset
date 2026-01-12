def distinct(n, arr):
  arr.sort()
  count = 1

  for i in range(1, n):
    if arr[i] != arr[i-1]:
      count += 1
  
  return count

if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))
  print(distinct(n, arr))
