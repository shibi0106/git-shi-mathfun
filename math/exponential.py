def EXP(A, B):
    Exp_result = 1
    for _ in range(abs(B)):
        Exp_result *= A
    if B < 0:
        Exp_result = 1 / Exp_result
    return Exp_result
A = float(input("Enter the base (A): "))
B = int(input("Enter the exponent (B): "))
Exp_result = EXP(A, B)
print(f"{A} raised to the power {B} is: {Exp_result}")
