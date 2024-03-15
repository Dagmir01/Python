numbers = []
for i in range(5):
    number = float(input("Введите число: "))
    numbers.append(number)
average = sum(numbers) / len(numbers)
print("Среднее значение введенных чисел:", average)