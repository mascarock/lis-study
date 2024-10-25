import matplotlib.pyplot as plt
import numpy as np
import time
from bisect import bisect_left
import logging

# Configure logging for detailed outputs
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Optimized function with O(n log n) complexity
def find_longest_increasing_subsequence_optimized(arr):
    n = len(arr)
    if n == 0:
        logging.info("The input list is empty.")
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

    logging.info(f"Longest Increasing Subsequence: {result[::-1]}")
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

    # Reconstruct the subsequence
    max_length = max(dp)
    max_index = dp.index(max_length)
    result = []
    while max_index != -1:
        result.append(arr[max_index])
        max_index = prev[max_index]
    
    return result[::-1]

# Function to check if an array is strictly increasing
def is_increasing_subsequence(arr):
    return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))

# Function to compare results of both algorithms
def compare_algorithms_on_various_inputs():
    test_cases = {
        "Random List": np.random.randint(1, 100, size=20).tolist(),
        "Sorted List": list(range(1, 21)),
        "Reversed List": list(range(20, 0, -1)),
        "Constant Values": [5] * 20,
        "Alternating Peaks": [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91],
        "Zigzag": [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]
    }

    for description, arr in test_cases.items():
        print(f"\nTesting: {description}")
        print(f"Input: {arr}")
        
        result_n_squared = find_longest_increasing_subsequence_n_squared(arr)
        result_optimized = find_longest_increasing_subsequence_optimized(arr)

        print(f"O(n^2) Result: {result_n_squared}")
        print(f"O(n log n) Result: {result_optimized}")

        # Verify that both results are strictly increasing and have the same length
        assert is_increasing_subsequence(result_n_squared), "O(n^2) result is not strictly increasing!"
        assert is_increasing_subsequence(result_optimized), "O(n log n) result is not strictly increasing!"
        assert len(result_n_squared) == len(result_optimized), (
            f"Mismatch in LIS lengths for {description}! "
            f"O(n^2) length: {len(result_n_squared)}, O(n log n) length: {len(result_optimized)}"
        )

    print("\nAll test cases passed successfully!")

# Run the comparison
compare_algorithms_on_various_inputs()

# Function to simulate time measurements for various input sizes
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
