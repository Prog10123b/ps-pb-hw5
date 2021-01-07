# Задача #3: Последовательность Фибоначчи

def generate_fib_row(end, lenght):

    row = [1, 1]
    new_num = 2

    while (end == -1 or new_num < end) and (len(row) < lenght or lenght == -1):
        row.append(new_num)
        new_num = row[len(row) - 2] + row[len(row) - 1]
    
    return row


def get_mod_eq_nums(nums, num, mod):
    
    res = []
    reqR = num % mod

    for i in nums:
        if i % mod == reqR:
            res.append(i)
    
    return res


fib_row = generate_fib_row(10000000, -1)
mod2_eq = get_mod_eq_nums(fib_row, 2, 2)
allNumSum = 0
allMod2EqNumsTxt = ''

for i in mod2_eq:
    allNumSum += i

for i in mod2_eq:
    allMod2EqNumsTxt += str(i) + '\n'

print(f"""Анализ ряда фибоначи до 10 000 000:
Длинна: {len(fib_row)}
Сумма всех четных элементов: {allNumSum}
Все четные элементы: 
{allMod2EqNumsTxt}Предпоследнее число последовательности: {fib_row[len(fib_row) - 2]}""")
