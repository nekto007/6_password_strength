import re
import os, sys
check = 1


def get_password_strength(password):
    global check
    if re.search('.\d', password):
        check += 1
        print('1')
    if re.search('[a-z]', password):
        check += 1
    if re.search('[A-Z]', password):
        check += 2
    if re.search('.\W', password):
        check += 2
        print(2)
    if len(password) >= 8:
        check += 1
    check = check_password_blacklist(password, check)


def check_password_blacklist(password, check):
    file = open('blacklist.txt', 'r').read().split()
    if str(password) in file:
        check = 1
    else:
        check += 2
    return check


if __name__ == '__main__':
    password = input('Введите Ваш пароль: ')
    os.system('clear')
    get_password_strength(password)
    print('Сложность Вашего пароля: %s/10' % (check))
