# Generate the plot and save it with a feasible name
import matplotlib.pyplot as plt
import numpy as np
import time
from bisect import bisect_left

# Optimized function with O(n log n) complexity
def find_longest_increasing_subsequence_optimized(arr):
    n = len(arr)
    if n == 0:
        return []
    tails = []
    prev = [-1] * n
    indices = []
    
    for i in range(n):
        pos = bisect_left(tails, arr[i])
        if pos == len(tails):
            tails.append(arr[i])
            indices.append(i)
        else:
            tails[pos] = arr[i]
            indices[pos] = i
        prev[i] = indices[pos - 1] if pos > 0 else -1

    result = []
    k = indices[len(tails) - 1]
    while k >= 0:
        result.append(arr[k])
        k = prev[k]

    return result[::-1]

# Original O(n^2) function for comparison
def find_longest_increasing_subsequence_n_squared(arr):
    n = len(arr)
    dp = [1] * n
    prev = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    return dp

def run_time_measurements():
    ns = list(range(10, 300, 10))  # Different input sizes
    n_squared_times = []
    n_log_n_times = []

    for n in ns:
        arr = np.random.randint(1, 100, size=n).tolist()

        # Measure O(n^2) function time
        start_time = time.time()
        find_longest_increasing_subsequence_n_squared(arr)
        n_squared_times.append(time.time() - start_time)

        # Measure O(n log n) function time
        start_time = time.time()
        find_longest_increasing_subsequence_optimized(arr)
        n_log_n_times.append(time.time() - start_time)

    return ns, n_squared_times, n_log_n_times

# Get data for plotting
ns, n_squared_times, n_log_n_times = run_time_measurements()

# Create the plot for time complexity comparison
plt.figure(figsize=(10, 6))
plt.plot(ns, n_squared_times, label='O(n^2) - Original Approach', marker='o')
plt.plot(ns, n_log_n_times, label='O(n log n) - Optimized Approach', marker='x')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity Comparison: O(n^2) vs O(n log n)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the plot with a feasible name
plot_filename = "complexity_comparison.png"
plt.savefig(plot_filename)

# Display the plot
plt.show()

# Return the filename for reference
plot_filename
