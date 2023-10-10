# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"

## Виконав: Троян Ростислав Віталійович (Група ІР-23)

### Лабораторна робота №2 (Варіант 2 Рівень 1)

### Варіант 2

Припустимо, компанія, в якій ви працюєте, розробляє електронний календар. У календарі є функція, що показує, коли різні команди програмістів будуть зайняті протягом будь-якої зустрічі.

Ті періоди, коли команда зайнята, на календарі позначені як діапазони часу, наприклад, з 10:00 до 12:30 або з 12:30 до 13:00. У вашій програмі проміжок часу представлений у вигляді пари з двох цілих чисел. Число означає номер 30-хвилинного блоку, який йде після 9:00 ранку. Наприклад, кортеж (2, 4) означає діапазон з 10:00 до 11:00, а (0, 1) - це проміжок 9:00-9:30.

Вам потрібно написати функцію, яка повинна спростити вивід інформації таким чином, що якщо команда зайнята в проміжках з 10:00 до 12:30 і з 12:30 до 13:00, то це має відображатись  як 10: 00-13: 00. 

Приклад: 

на вході вашої функції невпорядкований масив з кортежів `[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]`, 

Результат:
Ваша функція має повернути впорядкований масив  `[(0, 1), (3, 8), (9, 12)]`.  
  
Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` та перевірити роботу вашої функції на прикладах, наведених вище


***
