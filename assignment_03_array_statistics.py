# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def calculate_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

def calculate_max(arr):
    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
    return maximum

def calculate_min(arr):
    minimum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num
    return minimum

def calculate_average(arr):
    return calculate_sum(arr) / len(arr)

def main():
    try:
        n = int(input("How many numbers? "))
    except ValueError:
        print("Error: N must be a positive integer.")
        return

    if n <= 0:
        print("Error: N must be a positive integer.")
        return
    
    arr = []
    for i in range(1, n + 1):
        val = float(input(f"Enter number {i}: "))
        arr.append(val)
        
    print("\nResults:")
    print(f"Sum:     {calculate_sum(arr):g}")
    print(f"Average: {calculate_average(arr):g}")
    print(f"Maximum: {calculate_max(arr):g}")
    print(f"Minimum: {calculate_min(arr):g}")

if __name__ == "__main__":
    main()
