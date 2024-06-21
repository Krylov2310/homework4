task = 'Практическая работа по уроку "Организация программ и методы строк."'
avtor = 'Студент Крылов Эдуард Васильевич'
thanks = 'Благодарю за внимание :-)'
print()
print(task)
print(avtor)
print()
my_string = str(input('Введите любой текст: '))
print('Длина введенного текста: ', len(my_string), 'символов')
print('Верхний регистр:', my_string.upper())
print('Нижний регистр:', my_string.lower())
print('Удалены все пробелы:', my_string.replace(' ', ''))
print('Первый символ:', my_string[0])
print('Последний символ:', my_string[-1])
print()
print(thanks)
