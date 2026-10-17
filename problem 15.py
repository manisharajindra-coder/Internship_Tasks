# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
  pass


def main():
 
  n = int(input().strip())

  word_counts = OrderedCounter()
  for _ in range(n):
    word = input().strip()
    word_counts[word] += 1

  
  print(len(word_counts))
  
  print(*(word_counts.values()))


if __name__ == "__main__":
  main()