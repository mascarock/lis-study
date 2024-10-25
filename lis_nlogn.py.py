# second approach - O(nlogn)
import logging
from bisect import bisect_left

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def find_longest_increasing_subsequence_optimized(arr):
    n = len(arr)
    if n == 0:
        logging.info("The input list is empty.")
        return []
    
    logging.info(f"Input array: {arr}")
    
    # 'tails' to store the increasing subsequence
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
        
        # Log the progress
        logging.info(f"Element {arr[i]} at index {i}: placed at position {pos} in tails.")
        logging.info(f"Current tails: {tails}")
        logging.info(f"Previous indices: {prev}")

    # Reconstruct the LIS
    result = []
    k = indices[len(tails) - 1]
    while k >= 0:
        result.append(arr[k])
        k = prev[k]

    logging.info(f"Longest Increasing Subsequence: {result[::-1]}")
    return result[::-1]

# Original list
numbers = [9, 44, 32, 12, 7, 45, 31, 98, 35, 41, 8, 20, 27, 32, 83, 64, 61, 28, 39, 93, 29, 92, 17]

# Find the longest increasing subsequence using the optimized function
result_optimized = find_longest_increasing_subsequence_optimized(numbers)
print("Subsecuencia creciente más larga:", result_optimized)
