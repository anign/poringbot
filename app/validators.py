BAD_SYMBOLS = "\йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ ,./"


def is_nick_valid(n):
    for i in nick:
        if i in BAD_SYMBOLS:
            raise TypeError ('Ник содержит недопустимые символы!')
    return True

def format_nickname_tg(nick):
    """ Приводит введенный ник в телеграмме в стандартный вид @nickname """

    if is_nick_valid(nick):
        nick = nick.strip()
        if '@' not in n:
            return '@' + nick
        return nick

def is_nickname_is_exist(nick):
    pass

if __name__ == '__main__':
    pass