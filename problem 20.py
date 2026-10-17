# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def solve():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    arr = input_data[2:2+n]
    A = set(input_data[2+n : 2+n+m])
    B = set(input_data[2+n+m : 2+n+2*m])
    happiness = 0
    for x in arr:
        if x in A:
            happiness += 1
        elif x in B:
            happiness -= 1
            
    print(happiness)

if __name__ == '__main__':
    solve()