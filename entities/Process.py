import time

from utils.utils import clean_bytes_string, execute_shell, string_to_list


class Process:
    def __init__(self, name, filter, start_commands, category):
        self.name = name
        self.filter = filter
        self.start_commands = start_commands
        self.category = category

    def get_pids(self):
        (output, err) = execute_shell(self.filter)
        if err:
            return err
        output_cleaned = clean_bytes_string(output)
        output_list = output_cleaned.replace('\t', '|').replace(
            '\n', '|').replace(' ', '|').split('|')
        output_list_cleaned = [i for i in output_list if i]
        return string_to_list(output_cleaned)

    def kill(self):
        pids = self.get_pids()
        if self.isUp():
            print("matando proceso {}".format(self.name))
            processes = ' '.join(pids)
            command = 'kill -9 {}'.format(processes)
            execute_shell([command])

    def start(self):
        if len(self.get_pids()) == 0:
            print("levantando proceso {}".format(self.name))
            (output, err) = execute_shell([self.start_commands])
            if err:
                return err
            return clean_bytes_string(output)
        else:
            print("sin hacer nada porque esta arriba con estos pids {}".format(
                self.get_pids()))

    def restart(self):
        self.kill()
        time.sleep(5)
        self.start()

    def isUp(self):
        up = False
        if len(self.get_pids()) > 0:
            up = True
        return up
