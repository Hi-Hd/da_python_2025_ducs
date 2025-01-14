import matplotlib.pyplot as plt
import random
def linearSearch(arr: list[int], key: int):
    points = 0
    for i in arr:
        points += 1
        if i == key:
            return [key, points]
    return [key, points]

def createRandomList(n: int)-> list[int]:
    arr = []
    for i in range(n):
        arr.append(int(random.random() * n))
    return arr

def runLinearSearch(arr: list[int], n: int) -> list[list[int]]:
    ans = []
    for i in range(n):
        ans.append(linearSearch(arr, int(random.random() * n)))
    return ans
        
def plotTheArray(arr: list[int]):
    newArr = [subarr[0] for subarr in arr]
    
    maximumValue = -1
    maxInd = float("-inf")
    minumumValue = len(arr) + 1
    minInd = float("inf")
    avgValue = int(sum(newArr) / len(arr))
    avgInd = -1
    for i in range(len(arr)):
        if maximumValue < newArr[i]:
            maximumValue = newArr[i]
            maxInd = i
        if minumumValue > newArr[i]:
            minumumValue = newArr[i]
            minInd = i
        if avgValue + int(n / 20) >= newArr[i] and avgValue - int(n / 20) <= newArr[i]:
            avgInd = i
    ans = []
    print("maximum = ", arr[maxInd])
    print("minimum = ", arr[minInd])
    print("average index = ", arr[avgInd])
    ans.append(arr[maxInd])
    ans.append(arr[minInd])
    if avgInd != -1:
        ans.append(arr[avgInd])
    x = [i[0] for i in ans]
    y = [i[1] for i in ans]
    
    plt.scatter(x,y, marker='o')
    
    plt.xlabel('key')
    plt.ylabel('tries')
    plt.title('scatter plot of key and tries required for it')
    
    plt.show()

n = 1000

arr = createRandomList(n)
print(arr)
ans = runLinearSearch(arr,n)
print(ans)
plotTheArray(ans)
