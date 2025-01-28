import random
import matplotlib.pyplot as plt

def insertionSort(arr: list[int]) -> tuple[list[int], int]:
    operations = 0
    for i in range(1, len(arr)):
        j = i
        while j > 0:
            operations += 1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr, operations

def randomGeneratedList(n: int) -> list[int]:
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 5*n))
    return arr

# Generate and sort 10 randomly generated lists of random sizes
operations_list = []
list_sizes = []
for i in range(10):
    size = random.randint(50, 150)  # Random size between 50 and 150
    list_sizes.append(size)
    arr = randomGeneratedList(size)
    sorted_arr, operations = insertionSort(arr)
    operations_list.append(operations)
    print(f"List {i+1} (size {size}): {operations} operations")

# Plot the number of operations against the size of the list
plt.figure(figsize=(10, 6))
plt.scatter(list_sizes, operations_list, marker='o', color='b')
plt.title('Number of Operations to Sort Randomly Generated Lists')
plt.xlabel('Size of List')
plt.ylabel('Number of Operations')
plt.grid(True)
plt.show()
