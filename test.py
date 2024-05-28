from matplotlib import pyplot as plt
from matplotlib import patches

values = [10, 20, 30, 40, 50, 60]
x = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
y = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]


# Функция для определения цвета на основе значения
def get_color(value):
    if value < 20:
        return 'red'
    elif value < 40:
        return 'orange'
    elif value < 60:
        return 'green'
    else:
        return 'blue'


# Создаем фигуру и оси
fig, ax = plt.subplots()

# Рисуем квадраты с разными цветами
for i in range(6):
    color = get_color(values[i])
    square = patches.Rectangle((x[i], y[i]), 0.5, 0.5, edgecolor='black', facecolor=color)
    ax.add_patch(square)

# Настраиваем границы осей
ax.set_xlim(0, 7)
ax.set_ylim(-5, 2)
ax.set_aspect('equal')

# Показываем график
plt.show()
