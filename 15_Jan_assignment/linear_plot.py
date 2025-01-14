import matplotlib.pyplot as plt
def linearSearch(arr: list[int], key: int):
    points = 0
    for i in arr:
        points += 1
        if i == key:
            return [key, points]
    return [key, points]

def createList(n : int):
    arr = []
    for i in range(1, n + 1):
        arr.append(i)
    return arr
def runLinearSearch(arr: list[int], n: int) -> list[list[int]]:
    ans = []
    for i in range(1, n + 1):
        ans.append(linearSearch(arr, i))
    return ans
def plotTheArray(arr: list[int]):
    x = [i[0] for i in arr]
    y = [i[1] for i in arr]
    
    plt.scatter(x,y, marker='o')
    
    plt.xlabel('key')
    plt.ylabel('tries')
    plt.title('scatter plot of key and tries required for it')
    
    plt.show()

n = 100
arr = createList(n)
ans = runLinearSearch(arr, n)
plotTheArray(ans)