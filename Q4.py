def fibonacci_first_100():
    fib = [1, 1]  # Start with the first two Fibonacci numbers
    
    # Generate up to the 100th Fibonacci number
    for i in range(2, 100):
        fib.append(fib[i - 1] + fib[i - 2])
    
    # Print the resulting Fibonacci numbers
    for index, value in enumerate(fib, start=1):
        print(f"F({index}) = {value}")

if __name__ == "__main__":
    fibonacci_first_100()
