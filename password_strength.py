import re


def get_password_strength(password):
    check = 1
    if re.search('.\d', password):
        check += 1
    if re.search('[a-z]', password):
        check += 1
    if re.search('[A-Z]', password):
        check += 2
    if re.search('.\W', password):
        check += 2
    if len(password) >= 8:
        check += 1
    with open('blacklist.txt', 'r') as blacklist:
        check += 2
        for i in blacklist:
            if password in i:
                check = 1
                break
    print('Сложность вашего пароля: ', check)


if __name__ == '__main__':
    get_password_strength(input('Введите пароль: '))
