def max_experience(levels, experience):
    # Ініціалізація таблиці для зберігання максимального досвіду
    max_exp_table = [[0] * i for i in range(1, levels + 1)]

    # Заповнення таблиці
    for i in range(levels - 1, -1, -1):
        for j in range(i + 1):
            if i == levels - 1:
                max_exp_table[i][j] = experience[i][j]
            else:
                max_exp_table[i][j] = experience[i][j] + max(max_exp_table[i + 1][j], max_exp_table[i + 1][j + 1])

    # Максимальний досвід для початкового рівня
    return max_exp_table[0][0]


# Зчитування вхідних даних
with open("career.in", "r") as file:
    levels = int(file.readline().strip().split()[0])
    experience = [list(map(int, file.readline().split())) for _ in range(levels)]

# Обчислення та виведення результату
result = max_experience(levels, experience)
with open("career.out", "w") as file_out:
    file_out.write(str(result))
