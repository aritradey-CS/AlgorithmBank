import sys

def matrix_chain_multiplication(dimensions):
    n = len(dimensions) - 1

    # Create a table to store the minimum number of multiplications needed
    # to compute the product of matrices from i to j
    dp = [[0] * n for _ in range(n)]

    # Fill the table diagonally, considering different chain lengths
    for chain_len in range(2, n + 1):
        for i in range(n - chain_len + 1):
            j = i + chain_len - 1
            dp[i][j] = sys.maxsize

            # Iterate through all possible ways to split the chain
            for k in range(i, j):
                # Compute the number of multiplications needed for the split
                count = dp[i][k] + dp[k+1][j] + dimensions[i] * dimensions[k+1] * dimensions[j+1]
                if count < dp[i][j]:
                    dp[i][j] = count

    return dp[0][n-1]

# Example usage
dimensions = [10, 30, 5, 60]
minimum_multiplications = matrix_chain_multiplication(dimensions)

print("Matrix Dimensions:", dimensions)
print("Minimum number of multiplications:", minimum_multiplications)
