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
    x = [i[0] for i in arr]
    y = [i[1] for i in arr]
    
    plt.scatter(x,y, marker='o')
    
    plt.xlabel('key')
    plt.ylabel('tries')
    plt.title('scatter plot of key and tries required for it')
    
    plt.show()

n = 100
arr = createRandomList(n)
print(arr)
damn = runLinearSearch(arr, n)
print(damn)
plotTheArray(damn)


    
