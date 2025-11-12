def square_root(number, tolerance=1e-10):
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    if number == 0:
        return 0
    guess = number / 2.0
    while abs(guess * guess - number) > tolerance:
        guess = (guess + number / guess) / 2.0
    return guess

n = float(input("Enter a number to find its square root: "))
root_sq = square_root(n)
print(f"The square root of {n} is approximately: {root_sq}")
