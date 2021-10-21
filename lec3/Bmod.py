def func(Matrix):
    inArray = list(map(int, input().split()))
    for i in range(inArray[1]):
        Matrix[inArray[0]-1][inArray[i+2]-1] = 1

def getChild(node,Matrix,close): # 子ノードを小さい順に返す．[1,2,3]
    result = []
    vec = Matrix[node-1][:]
    for num, item in enumerate(vec):
        idx = num + 1
        if item == 0:
            continue
        else:
            if not idx in close:
                 result.append(idx)
    return result

def setClose(list, close):
    for item in list:
        close.append(item)

def setOpen(list, open): # list は小さい順
    for item in reversed(list):
        open.append(item)

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
    close = []
    finite = []
    init = 1
    # open.append([0,init])
    open.append(init)
    time = 1
    output = []
    for i in range(n):
        vec = [i+1,0,0]
        output.append(vec)

    # close.append(init)
    state = 1
    while(open):
        x = open[-1]
        close.append(x)
        if output[x-1][1] == 0:
            output[x-1][1] = time
        if x == 1 and close != [1]:
            break
        child = getChild(x,Matrix,close)
        if not child:
            open.pop()
            time += 1
            if output[x-1][2] == 0:
                output[x-1][2] = time
            # if state == 1:
            #     state = 0
            #     time += 1
            continue
        else:
            # setClose(child,close)
            setOpen(child,open)
            time += 1
            # if state == 0:
            #     state = 1
                # time -= 1

    output[0][2] = time
    
    for i in output:
        print(*i)


if __name__ == "__main__":
    main()