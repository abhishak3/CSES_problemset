def perm(n):
  if n == 1:
    return 1
  if n <= 3:
    return "NO SOLUTION"
  
  ans = [0] * n
  ele = 1
  
  for i in range(1, n, 2):
    ans[i] = ele
    ele += 1
  
  for i in range(0, n, 2):
    ans[i] = ele
    ele += 1
  
  return " ".join(map(str, ans))

if __name__ == "__main__":
  n = int(input())
  print(perm(n))