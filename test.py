import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Загружаем изображение
image_path = 'media/pumproom.png'
img = mpimg.imread(image_path)

# Создаем фигуру и ось
fig, ax = plt.subplots()

# Отображаем изображение
ax.imshow(img)

# Отключаем оси
ax.axis('off')

# Определяем текст и его позиции
variable_value1 = 3.14
variable_value2 = 2.718
text1 = f'Variable 1: {variable_value1:.2f}'
text2 = f'Variable 2: {variable_value2:.2f}'

# Добавляем текст на изображение
ax.text(10, 30, text1, fontsize=8, color='white', bbox=dict(facecolor='black', alpha=0.5))
ax.text(10, 150, text2, fontsize=8, color='red', bbox=dict(facecolor='black', alpha=0.2, boxstyle='round'))

# Сохраняем изображение с новым именем
output_image_path = 'media/test.png'
plt.savefig(output_image_path, bbox_inches='tight', pad_inches=0, dpi=300)

# Показываем изображение с добавленным текстом
plt.show()
