"""
Get Back to this question.
Find Median and then absolute sum
"""
def calculate_abs(arr, x):
  ans = 0
  for num in arr:
    ans += abs(num - x)
  return ans

def sticks_length(n, arr):
  arr.sort()
  return calculate_abs(arr, arr[n >> 1])

if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))
  print(sticks_length(n, arr))