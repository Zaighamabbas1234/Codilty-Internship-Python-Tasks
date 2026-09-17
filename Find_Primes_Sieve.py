# Problem Statement:
# Write a Python function to find Prime Numbers.

# Description:
# Write a function "find_primes (n)" that returns a list of all prime numbers less than "n". Optimize the function for efficiency.

# Solution:
# A Prime number is a positive integer that is divisible only by itself and 1.
# For example: 2,3,5,7.
# A Composite number is a positive integer greater than (1) that has more than two positive factors. In other words, a composite number can be divided evenly by numbers other than (1) and itself.

# Point to be Note:
# The integer (1) is neither a Prime number nor a Composite number. To find all Prime numbers less than (n) with maximum efficiency, I should use the Sieve of Eratosthenes which is much faster than checking each number individually.

# Sieve of Eratosthenes algorithm:
# The Sieve of Eratosthenes is an efficient algorithm used to find all prime numbers less than a given number (n). Instead of checking each number individually for primality, it repeatedly marks the multiples of each prime number as composite (non-prime). The numbers that remain unmarked are prime numbers.

# Find_Primes_Sieve Code:

# Defines a function named find_primes. The function takes one parameter (n) which is the upper limit. It will return all prime numbers less than (n).
def find_primes(n):
    if n <= 2: # Checks whether (n) is less than or equal to 2.
        return [] # Since there are no prime numbers less than 2, the function returns an empty list [].

    # Assume all numbers are prime initially:
    
    is_prime = [True] * n # Every element is initially set to True, assuming every number is prime.
    # is_prime = [True, True, True, True, True, True, True, True, True, True]
    is_prime[0] = is_prime[1] = False # Marks 0 and 1 as not prime.
    # is_prime = [False, False, True, True, True, True, True, True, True, True]
    
    # Mark multiples of each prime as non-prime:
    
    for i in range(2, int(n ** 0.5) + 1): # Starts a loop from 2 up to the square root of (n). (n**0.5) calculates the square root. int() converts it to an integer. (+1) ensures the last value is included.
        if is_prime[i]: # The line is a conditional statement. It checks whether the number i is still considered prime.
            for j in range(i * i, n, i): # Starts another loop to mark multiples of i. Begins at (i*i) instead of (2*i).
                is_prime[j] = False # Marks every multiple of (i) as not prime.
            
    # Return all Prime Numbers:
    return [i for i in range(2, n) if is_prime[i]] # This is called a list comprehension. Go through every number from (2) to (n - 1). If is_prime[i] is True, include i in the result. Return the completed list.

# Example usage:
print(find_primes(50))

# Complexities:
# Time Complexity: O(n log log n) (very efficient).
# Space Complexity: O(n).

# How the algorithm works (for n = 50)?
# Step 1: Assume every number from (2) to (49) is prime.
# Step 2: Mark multiples of (2) as non-prime.
# Step 3: Mark multiples of (3) as non-prime.
# Step 4: Skip (4) because it's already marked non-prime.
# Step 5: Mark multiples of (5) as non-prime.

# All remaining numbers marked True are prime numbers:
# [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

# This approach is known as the Sieve of Eratosthenes, one of the fastest algorithms for finding all prime numbers smaller than a given number.

# Submitted By: Zaigham Abbas.
# Submitted to: HR Codility.
# Dated: 08/06/2026.