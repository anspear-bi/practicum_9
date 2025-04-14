import math
input_num = float(input('Введите число больше 2: '))
while input_num < 2:
    input_num = float(input('Введите число больше 2: '))
else:
    sqrt_num = input_num
    while sqrt_num > 2:
        sqrt_num = math.sqrt(sqrt_num)
        print(sqrt_num)
