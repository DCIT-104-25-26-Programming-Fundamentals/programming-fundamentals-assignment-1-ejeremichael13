# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def generate_fibonacci(n):
    """Generates the first N terms of the Fibonacci sequence using a loop."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    for _ in range(2, n):
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
        
    return sequence

def is_fibonacci(num):
    """Checks if a given number belongs to the Fibonacci sequence using a loop."""
    if num < 0:
        return False
        
    a, b = 0, 1
    if num == a or num == b:
        return True
        
    while b < num:
        next_val = a + b
        a = b
        b = next_val
        if b == num:
            return True
            
    return False

def main():
   
    try:
        n = int(input("How many terms? "))
    except ValueError:
        print("Error: N must be a positive integer.")
        return
        
    if n <= 0:
        print("Error: N must be a positive integer.")
        return
        
    fib_sequence = generate_fibonacci(n)
 
    print(f"Fibonacci sequence: {' '.join(str(x) for x in fib_sequence)}")
    
    print()
    
    
    try:
        check_num = int(input("Enter a number to check: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return
        
    if is_fibonacci(check_num):
        print(f"{check_num} is a Fibonacci number.")
    else:
        print(f"{check_num} is NOT a Fibonacci number.")

if __name__ == "__main__":
    main()