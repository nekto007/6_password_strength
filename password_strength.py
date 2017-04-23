import re
import os
import getpass


def get_password_strength(password):
    point = 1
    if re.search('.\d', password):
        point += 1
    if re.search('[a-z]', password):
        point += 1
    if re.search('[A-Z]', password):
        point += 2
    if re.search('.\W', password):
        point += 2
    if len(password) >= 8:
        point += 1
    result = is_password_in_blacklist(password, point)
    return result


def is_password_in_blacklist(password, point):
    with open('blacklist.txt', 'r') as blacklist:
        blacklist = blacklist.read().split()
    if str(password) in blacklist:
        point = 1
    else:
        point += 2
    return point


if __name__ == '__main__':
    password = getpass.getpass(prompt='Введите Ваш пароль: ')
    result = get_password_strength(password)
    print('Сложность Вашего пароля: %s/10' % (result))
