"""
This question tests the maximum overlapping intervals types question
"""
def restaurant_customers(n, arr, dep):
  arr.sort()
  dep.sort()

  count = 0
  ans = 0
  j = 0

  for d in dep:
    while j < n and arr[j] < d: # assuming all arr and dep items are distinct (not considering 'arr[j] == d')
      count += 1
      j += 1
    
    ans = max(ans, count)
    
    if j == n:
      break

    count -= 1
  
  return ans


if __name__ == "__main__":
  n = int(input())
  arr, dep = [], []

  for _ in range(n):
    a, d = map(int, input().split())
    arr.append(a)
    dep.append(d)
  
  print(restaurant_customers(n, arr, dep))
