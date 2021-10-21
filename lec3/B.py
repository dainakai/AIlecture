def func(Matrix):
    inArray = list(map(int, input().split()))
    for i in range(inArray[1]):
        Matrix[inArray[0]-1][inArray[i+2]-1] = 1

def main():
    # 隣接行列
    n = int(input())
    Matrix = []
    for i in range(n):
        vec = []
        for j in range(n):
            vec.append(0)
        Matrix.append(vec)

    for idx in range(n):
        func(Matrix)

    # DFS
    open = []
    close = [0]
    finite = []
    init = 1
    open.append([0,init])
    time = 1
    output = []
    for i in range(n):
        vec = [i+1,0,0]
        output.append(vec)

    while 1:
        print(time, open, close)
        
        if not open:
            break
        # if 
        x = open[-1]
        if close[-1] != x[0]:
            if output[close[-1]-1][2] == 0:
            #     output[close[-1]-1][2] == 1
                output[close[-1]-1][2] = time
            close.pop(-1)
            time += 1
            continue
        vec = Matrix[x[1]-1][:]
        close.append(x[1])
        finite.append(x[1])
        open.remove(x)
        if output[x[1]-1][1] == 0:
        #     output[x[1]-1][1] == 1
            output[x[1]-1][1] = time
        
        for num, item in enumerate(reversed(vec)):
            node = len(vec) - num
            if item == 0:
                continue
            if not (node in finite):
                open.append([x[1],node])

        time += 1

    output[0][2] = time -1
    
    for i in output:
        print(*i)


if __name__ == "__main__":
    main()