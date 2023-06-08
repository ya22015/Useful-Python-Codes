import numpy as np

def get_non_primes(a, b):
    # Make sure a and b are positive integers
    try:
        a, b = int(a), int(b)
        if a <= 0 or b <= 0:
            raise ValueError
    except ValueError:
        print("Error: Please enter two positive integers.")
        return []

    # Make sure a <= b
    if a > b:
        a, b = b, a

    # Find all non-prime numbers between a and b
    non_primes = []
    for n in range(a, b+1):
        if n < 2:  # 1 is not a prime number
            non_primes.append(n)
        elif all(n % i != 0 for i in range(2, int(np.sqrt(n))+1)):
            continue  # n is prime, skip to the next number
        else:
            non_primes.append(n)

    return non_primes


def main():
    # Get input from user
    a = input("Enter the first positive integer: ")
    b = input("Enter the second positive integer: ")

    # Get list of non-prime numbers
    non_primes = get_non_primes(a, b)

    # Output the list with 10 numbers per line
    if non_primes:
        print("Non-prime numbers between {} and {}:".format(a, b))
        for i, n in enumerate(non_primes):
            if i % 10 == 9:
                print("{:4d}".format(n))
            else:
                print("{:4d}".format(n))
    else:
        print("Exiting program.")
    
if __name__ == '__main__':
    main()
