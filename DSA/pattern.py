def pattern(n):
    if n == 0:
        return
    pattern(n - 1)
    print("*" * n)

pattern(5)