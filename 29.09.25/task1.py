def greet(name):
    print(f"привет, {name}!")
u_name = input("введите своё имя: ")
greet(u_name)


def square(n):
    return n**2
n = int(input("введите число для возведения в квадрат: "))
print("результат:", square(n))


def max_of_two(x, y):
    if x>y:
        return x
    elif x<y:
        return y
    else:
        print("числа равны")
        return None
a=int(input("введите первое число: "))
b=int(input("введите второе число: "))
r=max_of_two(a, b)
if r is not None:
    print("наибольшее число:", r)