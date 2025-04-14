x = int(input("Введите натуральное число x: "))
count = 0
for a in range(1, int(x ** 0.5) + 1):
    b_squared = x - a ** 2
    b = int(b_squared ** 0.5)  

    if b_squared > 0 and b ** 2 == b_squared and a <= b:
        count += 1

print(f"Количество способов представления числа {x} в виде суммы квадратов двух натуральных чисел: {count}")
