"""
This question is to find max non overlapping intervals
"""
def movies(n, intervals):
  intervals.sort(key=lambda x : x[1])
  count = 1

  end = intervals[0][1]

  for i in range(1, n):
    curr_start, curr_end = intervals[i]

    if curr_start >= end:
      count += 1
      end = curr_end
  
  return count


if __name__ == "__main__":
  n = int(input())
  interval = []

  for _ in range(n):
    interval.append(list(map(int, input().split())))
  
  print(movies(n, interval))