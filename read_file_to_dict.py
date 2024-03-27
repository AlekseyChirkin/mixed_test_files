data_text = """
Я их рот наоборот различными способами,
сколько можно испытывать проблемы с кодировкой?
Либо тут что-то не так, либо как-то иначе =)
Пробую записать, потом прочитать, должно же сработать хоть так?..
"""

with open('very_impotent_text.txt', 'w', encoding='utf-8') as f:
    f.write(data_text)

with open('very_impotent_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    print(text)
