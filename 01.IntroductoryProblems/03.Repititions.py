dna = input()
n = len(dna)

i = 0
ans = 0

while i < n:
  curr = dna[i]
  ln = 0

  while i < n and curr == dna[i]:
    ln += 1
    i += 1
  
  ans = max(ans, ln)

print(ans)