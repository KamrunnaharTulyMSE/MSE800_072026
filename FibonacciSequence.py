# Function to print Fibonacci series
def fibonacci(n):
    a = 0
    b = 1

    print("Fibonacci Series:")

    while a <= n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c

    print()


# Function to calculate factorial
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


# Main function
def main():
    n = int(input("Enter a number: "))

    fibonacci(n)

    print("Factorial:", factorial(n))


# Start the program
main()