# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
# Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.

words = ['attribute', 'класс', 'функция', 'type']
for i in words:
    try:
        word = eval(f"b'{i}'")
    except SyntaxError:
        print(f'Слово "{i}" состоит из символов не относящихся к ASCII(кириллица), поэтому его нельзя записать в байтовом виде.')
