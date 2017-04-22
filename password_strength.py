import re
import os, sys
point = 1

def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')


def get_password_strength(password, point):
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
    blacklist = open('blacklist.txt', 'r').read().split()
    if str(password) in blacklist:
        point = 1
    else:
        point += 2
    return point


if __name__ == '__main__':
    password = input('Введите Ваш пароль: ')
    clear_console()
    result = get_password_strength(password, point)
    print('Сложность Вашего пароля: %s/10' % (result))
