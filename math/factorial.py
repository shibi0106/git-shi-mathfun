def factorial(nm):
    if nm < 0:
       raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, nm + 1):
        result *= i
    return result

n = int(input("Enter a number to find its factorial: "))
f = factorial(n)
print(f"The factorial of {n} is: {f}")
