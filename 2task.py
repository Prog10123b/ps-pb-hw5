# Задача #2: FizzBuzz

sym = 0
low_bord = 1000
high_bord = 20000

for i in range(low_bord, high_bord):
    if i % 3 == 0 and i % 5 == 0:
        sym += i
    
print(f'Сумма чисел в диапазоне между {low_bord} и {high_bord}, которые делятся на 3 и на 5: {sym}')
