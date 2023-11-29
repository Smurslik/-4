import string          # модуль для більш зручної праці з строкою

# file_path = input("Введіть шлях(.txt): ")             # це перший варіант коду
file_path = '/Users/smurslik/Downloads/qweerasd.txt'    # це шлях до коду
try:
    with (open(file_path, "r") as file):                # open функція для відкриття файлу
        content = file.read()
        word_count = {}

        content = content.translate(str.maketrans('', '', string.punctuation))         # вилучення знаків пунктуації
        words = content.split()                                                        # розділяє наш текст н слова і
                                                                                       # створює з них список
        for word in words:                                                             # проходимо по списку усіх слів
            if not word.isalpha():
                continue
            word = word.lower()                                                        # прибираємо великі літери
            if word in word_count:                                                     # якщо слово є в словнику
                word_count[word] += 1                                                  # збільшуємо яго значеня так як
            else:                                                                      # слово це ключ
                word_count[word] = 1                                                   # якщо слово вперше значення 1

        for word, count in word_count.items():                                         # виводимо значеня словнику
            print(f'"{word}"  {count}')

except FileNotFoundError:
    print("Nu tut gg")
except IsADirectoryError:
    print('qq')
