if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        command = input().split()
        cmd = command[0]
        args = command[1:]
        
        if cmd == "print":
            print(lst)
        else:
            getattr(lst, cmd)(*(int(x) for x in args))