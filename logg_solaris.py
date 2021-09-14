import sys
import logging


def lo():
    logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                        level=logging.DEBUG, filename=u'mylog.log')
    # Сообщение отладочное
    logging.debug(u'This is a debug message')
    # Сообщение информационное
    logging.info(u'This is an info message')
    # Сообщение предупреждение
    logging.warning(u'This is a warning')
    # Сообщение ошибки
    logging.error(u'This is an error message')
    # Сообщение критическое
    logging.critical(u'FATAL!!!')


class print_to_txt(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)