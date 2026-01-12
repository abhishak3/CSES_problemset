"""
This question is sorting + two pointers
"""
def ferris(n, x, weights):
  count = 0
  weights.sort()

  l, r = 0, n-1
  while l <= r:
    if weights[l] + weights[r] <= x:
      l += 1
      r -= 1
    else:
      r -= 1
    count += 1
  
  return count

if __name__ == "__main__":
  n, x = map(int, input().split())
  weights = list(map(int, input().split()))

  print(ferris(n, x, weights))