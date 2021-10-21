def func(Matrix):
    inArray = list(map(int, input().split()))
    for i in range(inArray[1]):
        Matrix[inArray[0]-1][inArray[i+2]-1] = 1

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

    for i in Matrix:
        print(*i)

if __name__ == "__main__":
    main()