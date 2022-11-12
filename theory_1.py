# users = {'login': 'login_1', 'password': 'password_1'}
# users['email'] = 'email_1'
# users['login'] = 'login_2'

# del users['login']
# a = users.pop('password')
# print(a)
#
# print(users)
# print(users.get('login_1', 'Такого ключа нету'))

# for key, value in users.items():
#     print(key, value)
#
# print()
#
# for key in users.keys():
#     print(key)
#
# print()
#
# for value in users.values():
#     print(value)

classmates = {
    '10 Б': {
        'Иванов': 15,
        'Петров': 16
    },
    '10 A': {
        'Cидиров': 14,
        'Пушкин': 15
    }
}


def recursive_search(dictionary: dict, search_by) -> str:
    """Рукурсивный поиск по вложенным словарям

    :param dictionary: словарь, по которому будет производиться поиск
    :param search_by: параметр, по которому будет производиться поиск
    :return: Результат поиска
    """
    if search_by in dictionary.keys():
        return dictionary[search_by]

    for value in dictionary.values():
        if type(value) == dict:
            search_by = recursive_search(value, search_by)

    if search_by is not None:
        return 'Нет элементов, удолетвор. условию'


search = input('Введите фамилию или класс:')
print(f'{search}: {recursive_search(classmates, search)}')