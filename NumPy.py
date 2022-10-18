import numpy as np

# Задача №1
print(f"Задача №1")
my_array = np.array([[1, 2, 3, 3, 1], [6, 8, 11, 10, 7]])
my_array = my_array.transpose()
print(f"Массив my_array\n{my_array}")
mean_a = my_array.mean(axis=0)
print(f"Массив mean_a\n{mean_a}\n")

# Задача №2
print(f"Задача №2")
a_centered = my_array-mean_a
print(f"Массив a_centered\n{a_centered}\n")

# Задача №3
print(f"Задача №3")
a = a_centered[:, 0]
b = a_centered[:, 1]
a_centered_sp = a@b
print(f"Значение a_centered_sp: {a_centered_sp}")
N = len(a_centered)
result = a_centered_sp/(N-1)
print(f"Результат деления a_centered_sp/(N-1) = {result}\n")

# Задача №4
print(f"Задача №4")
a_b_cov = np.cov(a, b)
print(f"Ковариация: {a_b_cov[0, 1]}")
