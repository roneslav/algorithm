# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"

## Виконав: Троян Ростислав Віталійович (Група ІР-23)

### Лабораторна робота №2 (Варіант 2 Рівень 1)

### Варіант 3
Для бінарного дерева знайдіть суму всіх глибин усіх вузлів. Глибина вузла - це кількість ребер, які потрібно пройти від кореня дерева, щоб досягти цього вузла.

Ваше завдання полягає в написанні функції, яка обчислює та повертає суми глибин для всіх вузлів у бінарному дереві

Приклад: Розглянемо таке бінарне дерево:

    1
   / \
  2   3
 / \
4   5
Глибина вузла 1 -0, глибина вузла 2 та 3 становить 1, а глибина вузлів 4 та 5 - 2. Сума глибин всіх вузлів дорівнює 0 + 1 + 1 + 2 + 2 = 6.

Функція отримує на вхід корінь бінарного дерева, який має наступний вигляд:

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

 Ваша функція має мати такий вигляд:  

def sum_of_depths(root: TreeNode) -> int:
    # ваш код
Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу TreeNode наступним чином:

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

***
