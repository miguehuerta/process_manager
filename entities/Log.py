import errno
import os
from os.path import exists


class Log:
    def __init__(self, PATH):
        file_exists = exists(PATH)
        if file_exists:
            self.PATH = PATH
        else:
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), PATH)

    def read(self):
        f = open(self.PATH, "r")
        str_file = f.read()
        return str_file.split('\n')

    # tail is an int
    def tail(self, tail):
        try:
            int(tail)
        except ValueError:
            print("the value provided in argument is not an integer")
            list_log = self.read()
        return list_log[len(list_log)-tail-1:len(list_log)-1]

    def size(self):
        return os.path.getsize(self.PATH)
