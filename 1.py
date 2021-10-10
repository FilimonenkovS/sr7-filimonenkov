try:
    n = int(input("Введите число: "))
except ValueError:
    print("Ошибка")
a=int(input("Введите целевую систему счисления:"))
if a==2:
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
        print(b)
if a==8:
    base = int(8)
    result = ""
    while n > 0:
        result = str(n % 8) + result
        n //= base
        print(result)
