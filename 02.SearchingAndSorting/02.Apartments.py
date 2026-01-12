def apartments(n, m, k, apartment, need):
  apartment.sort()
  need.sort()

  j = 0
  count = 0

  for i in range(len(need)):
    while j < len(apartment) and apartment[j] <= need[i] + k:
      if abs(apartment[j] - need[i]) <= k:
        count += 1
        j += 1
        break
      j += 1
    
  return count

if __name__ == "__main__":
  n, m, k = map(int, input().split())
  apartment = list(map(int, input().split()))
  need = list(map(int, input().split()))

  print(apartments(n, m, k, apartment, need))