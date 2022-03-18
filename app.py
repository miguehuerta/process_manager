import time

import constants as cons
from entities.Log import Log
from entities.Process import Process
from entities.ProcessGroup import ProcessGroup


def restart_services():
    pg = ProcessGroup(cons.SERVICES)
    process = pg.get_process_by_name('example')
    print(process.kill())
    print(process.start())


def main():
    restart_services()


if __name__ == '__main__':
    main()
