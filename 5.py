# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce

def_list = [x for x in range(2, 11, 2)]              # Заменил четные числа от 100 до 1000 на от 2 до 10,
                                                     # а то результат перемножения совсем не реальный)
print(reduce(lambda x, y: x * y, def_list))
