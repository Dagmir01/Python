import turtle

# Получаем длину стороны квадрата от пользователя
длина_стороны = int(input("Вдите длину стороны квадрата: "))

# Создаем экземпляр черепахи
черепаха = turtle.Turtle()

# Устанавливаем позицию черепахи в центр экрана
черепаха.penup()
черепаха.goto(-длина_стороны // 2, длина_стороны // 2)
черепаха.pendown()

# Рисуем квадрат
for _ in range(4):
    черепаха.forward(длина_стороны)
    черепаха.right(90)

# Не закрываем окно после отрисовки
turtle.done()