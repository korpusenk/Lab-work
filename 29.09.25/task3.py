def is_prime(n):
    if n<2:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True
n=int(input("введите число: "))
print("это простое число" if is_prime(n) else "это составное число")