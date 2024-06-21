def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

num = int(input("Введите целое неотрицательное число: "))

if num < 0:
    print("Введите целое неотрицательное число.")
else:
    result = factorial(num)
    print(f"Факториал числа {num} равен {result}.")