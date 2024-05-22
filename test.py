import matplotlib.pyplot as plt
import numpy as np

# Создаем данные для рисунка
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Создаем рисунок
fig, ax = plt.subplots()
ax.plot(x, y)

# Значение переменной
variable_value = np.pi
text_str = f'Variable value: {variable_value:.2f}'

# Выводим текст с аннотацией поверх рисунка
ax.annotate(text_str, xy=(1, np.sin(1)), xytext=(3, 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, bbox=dict(facecolor='yellow', alpha=0.5))

# Показываем рисунок
plt.show()
