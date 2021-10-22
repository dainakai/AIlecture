def getChildNode(node, adjListSet, close):
    childSet = []
    adjList = adjListSet[node-1]
    for idx in range(adjList[1]):
        childCand = adjList[2+idx]
        if childCand in close:
            continue
        else:
            childSet.append(childCand)

def main():
    n = int(input())
    adjListSet = []
    for i in range(n):
        adjListSet.append(list(map(int, input().split())))
    
    close = []
    open = []
