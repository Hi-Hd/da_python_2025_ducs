import random
import matplotlib.pyplot as plt
def makeArray(n: int) -> list[int]:
    arr = []
    for i in range(n):
        arr.append(int(random.random() * n))
    return arr

def linearSearch(arr: list[int], key: int):
    points = 0
    for i in arr:
        points += 1
        if i == key:
            return [key, points]
    return [key, points]

def runLinearSearch(arr: list[int], keys: list[int], n : int):
    ans = []
    for i in keys:
        ans.append(linearSearch(arr, i))
    ans.append(linearSearch(arr, n * 2))
    return ans
    
def plotTheArray(arr: list[int]):
    x = [i[0] for i in arr]
    y = [i[1] for i in arr]
    
    plt.scatter(x,y, marker='o')
    
    plt.xlabel('key')
    plt.ylabel('tries')
    plt.title('scatter plot of key and tries required for it')
    
    plt.show()

n = 30
arr = makeArray(n)
print(arr)
keys = arr
random.shuffle(keys)
ans = runLinearSearch(arr, keys, n)
plotTheArray(ans)