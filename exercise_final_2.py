import matplotlib.pyplot as plt
import numpy as np

def draw_branch(x, y, angle, length, depth):
    if depth == 0:
        return

    # Обчислюємо координати кінця гілки
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    # Малюємо гілку
    plt.plot([x, x_end], [y, y_end], color="brown", lw=depth)

    # Рекурсивно малюємо наступні гілки
    new_length = length * 0.7  # зменшуємо довжину гілки
    draw_branch(x_end, y_end, angle + np.pi / 4, new_length, depth - 1)  # права гілка
    draw_branch(x_end, y_end, angle - np.pi / 4, new_length, depth - 1)  # ліва гілка

# Налаштування вікна для малювання
plt.figure(figsize=(8, 8))
plt.axis('off')

# Глибина рекурсії (рівень фракталу)
depth = int(input("Введіть глибину рекурсії (рівень фракталу): "))

# Початкова точка і початкова гілка
initial_length = 100
draw_branch(0, 0, np.pi / 2, initial_length, depth)

plt.show()

