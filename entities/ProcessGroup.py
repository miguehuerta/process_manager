import time

from entities.Process import Process


class ProcessGroup:
    # receives a list of processes of any kind
    def __init__(self, process_group):
        if isinstance(process_group, list) and len(process_group) > 0:
            if isinstance(process_group[0], Process):
                self.process_group = process_group
            if isinstance(process_group[0], dict):
                self.process_group = []
                for process in process_group:
                    p = Process(process['name'], process['filter'],
                                process['start_commands'], process['category'])
                    self.process_group.append(p)

    def get_process_by_name(self, name):
        process = [i for i in self.process_group if i.name == name]
        if process[0]:
            return process[0]
        else:
            return False

    def get_processes_by_category(self, category):
        processes = [i for i in self.process_group if i.category == category]
        if processes:
            return processes
        else:
            return False

    # receive a list of process
    def kill_group(self):
        for process in self.process_group:
            process.kill()

    def start_group(self):
        for process in self.process_group:
            process.start()

    def restart_group(self):
        self.kill_group()
        time.sleep(5)
        self.start_group()
