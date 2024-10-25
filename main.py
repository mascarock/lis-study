# first approach - O(n^2)
def find_longest_increasing_subsequence(arr):
    n = len(arr)
    # dp[i] almacena la longitud de la subsecuencia más larga que termina en arr[i]
    dp = [1] * n
    # prev[i] almacena el índice del elemento anterior en la subsecuencia
    prev = [-1] * n
    
    # Encuentra la longitud de la subsecuencia más larga
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    # Encuentra el índice del último elemento de la subsecuencia más larga
    max_length = max(dp)
    max_index = dp.index(max_length)
    
    # Reconstruye la subsecuencia
    result = []
    while max_index != -1:
        result.append(arr[max_index])
        max_index = prev[max_index]
    
    return result[::-1]  # Invierte la lista para obtener el orden correcto

# Lista original
numbers = [9,44,32,12,7,45,31,98,35,41,8,20,27,32,83,64,61,28,39,93,29,92,17]

# Encuentra la subsecuencia creciente más larga
result = find_longest_increasing_subsequence(numbers)
print("Subsecuencia creciente más larga:", result)