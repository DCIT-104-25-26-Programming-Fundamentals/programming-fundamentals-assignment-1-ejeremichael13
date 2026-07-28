# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_matrix(matrix):
    
    for row in matrix:
        print("  ".join(f"{val:4}" for val in row))

def read_matrix(rows, cols):
    
    matrix = []
    for i in range(rows):
        while True:
            row_str = input(f"Enter row {i+1}: ")
         
            row_vals = [float(x) if '.' in x else int(x) for x in row_str.split()]
            if len(row_vals) != cols:
                print(f"Error: Expected {cols} values, got {len(row_vals)}. Try again.")
                continue
            matrix.append(row_vals)
            break
    return matrix

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed

def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    
   
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

def multiply_matrices(matrix1, matrix2):
    rows_a = len(matrix1)
    cols_a = len(matrix1[0])
    cols_b = len(matrix2[0])
    
    
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a): 
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def main():
    
    print("--- PART A: Transpose a Matrix ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    matrix = read_matrix(rows, cols)
    
    print("\nOriginal Matrix:")
    print_matrix(matrix)
    
    print("\nTransposed Matrix:")
    transposed = transpose_matrix(matrix)
    print_matrix(transposed)
    

    print("\n--- PART B: Add Two Matrices ---")
    print("Please enter two matrices of the same size.")
    r_add = int(input("Enter number of rows: "))
    c_add = int(input("Enter number of columns: "))
    
    print("\nMatrix 1:")
    mat1 = read_matrix(r_add, c_add)
    print("\nMatrix 2:")
    mat2 = read_matrix(r_add, c_add)
    
    print("\nSum of matrices:")
    sum_matrix = add_matrices(mat1, mat2)
    print_matrix(sum_matrix)
    
  
    print("\n--- PART C: Multiply Two Matrices ---")
    r_a = int(input("Enter number of rows for Matrix A: "))
    c_a = int(input("Enter number of columns for Matrix A: "))
    print("\nMatrix A:")
    mat_a = read_matrix(r_a, c_a)
    

    print(f"\nMatrix B must have {r_b} rows to multiply with Matrix A.")
    c_b = int(input("Enter number of columns for Matrix B: "))
    print("\nMatrix B:")
    mat_b = read_matrix(r_b, c_b)
    
    print("\nProduct of A x B:")
    product_matrix = multiply_matrices(mat_a, mat_b)
    print_matrix(product_matrix)

if __name__ == "__main__":
    main()