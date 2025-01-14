import matplotlib.pyplot as plt
import random

def linear_search(arr, key):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == key:
            return comparisons
    return comparisons

# Generate input data and count key comparisons
input_sizes = list(range(10, 101, 5))
best_case_comparisons = []
worst_case_comparisons = []
average_case_comparisons = []

for n in input_sizes:
    arr = list(range(1, n + 1))
    keys = arr + [n + 1]  # n successful keys + 1 unsuccessful key
    
    best_case = linear_search(arr, keys[0])
    worst_case = linear_search(arr, keys[-2])
    average_case = sum(linear_search(arr, key) for key in keys) / len(keys)
    
    best_case_comparisons.append(best_case)
    worst_case_comparisons.append(worst_case)
    average_case_comparisons.append(average_case)

# Plot the graph
plt.plot(input_sizes, best_case_comparisons, label='Best Case')
plt.plot(input_sizes, worst_case_comparisons, label='Worst Case')
plt.plot(input_sizes, average_case_comparisons, label='Average Case')

plt.xlabel('Input Size (n)')
plt.ylabel('Number of Comparisons')
plt.title('Key Comparisons in Linear Search')
plt.legend()
plt.show()
