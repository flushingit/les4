# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета
# для конкретных значений необходимо запускать скрипт с параметрами.


import sys

file_name, work_time, hours_pay, prem = sys.argv

print(f"Заработная плата {int(work_time) * int(hours_pay) + int(prem)} рублей")
