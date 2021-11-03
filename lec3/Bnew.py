def func(Matrix):
    inArray = list(map(int, input().split()))
    for i in range(inArray[1]):
        Matrix[inArray[0]-1][inArray[i+2]-1] = 1

def getChild(node,Matrix,close):
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

def main():
    n = int(input())
    Matrix = []
    for i in range(n):
        vec = []
        for j in range(n):
            vec.append(0)
        Matrix.append(vec)

    for idx in range(n):
        func(Matrix)

    output = []
    for i in range(n):
        vec = [i+1,0,0]
        output.append(vec)

    open = []
    close = []

    open.append(1)
    time = 1

    while(open):
        node = open[-1]
        if output[node -1][1] == 0:
            output[node-1][1] = time
        
        if getChild(node,Matrix,close):
            child = getChild(node,Matrix, close)[0]
            open.append(child)
            close.append(node)
            time += 1
            continue
        
        if not getChild(node,Matrix,close):
            close.append(node)
            time += 1
            if output[node-1][2] == 0:
                output[node-1][2] = time
            open.pop()
            continue

    for i in output:
        print(*i)


if __name__ == "__main__":
    main()