def Fibonacci_number(n):
    if n < 0:
        print("N must be possitive")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci_number(n-1) + Fibonacci_number(n-2)

print(Fibonacci_number(11))
