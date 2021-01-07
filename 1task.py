# Задача #1: множественная форма числительных

def plural_form(number, *args):
    result = None

    if len(args) == 3:

        if number == 1:
            result = str(number) + ' ' + args[0]
        elif 1 < number < 5:
            result = str(number) + ' ' + args[1]
        else:
            result = str(number) + ' ' + args[2] 
        
    return result
        
print(plural_form(1, 'яблоко', 'яблока', 'яблок'))
print(plural_form(2, 'яблоко', 'яблока', 'яблок'))
print(plural_form(11, 'студент', 'студента', 'студентов'))
print(plural_form(15, 'студент', 'студента', 'студентов'))
print(plural_form(3, 'студент', 'студента', 'студентов'))
