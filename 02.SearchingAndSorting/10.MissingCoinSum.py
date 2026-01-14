"""
Coverage Expansion greedy

We start with coverage [1..sm] and try to extend it.
'sm' means I can cover everything from 1 to sm.
If current coin is greater than sm + 1 then that cannot be covered.
"""
def missing_coin_sum(n, coins):
  coins.sort()
  sm = 0

  for i, coin in enumerate(coins, 1):
    if sm + 1 < coin:
      break
    sm += coin
    
  return sm + 1

if __name__ == "__main__":
  n = int(input())
  coins = list(map(int, input().split()))
  print(missing_coin_sum(n, coins))