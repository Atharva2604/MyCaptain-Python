terms = int(input("Enter the number of terms: "))

def fibonacci(n):
    
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci Series:")
for i in range(terms):
    print(fibonacci(i), end=" ")
