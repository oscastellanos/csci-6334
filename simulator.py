from OS import OS
from ProcessImage import ProcessImage
from collections import namedtuple
from ProcessState import ProcessState
from CPU import CPU
from queue import Queue
import csv

from OS import OS


class Simulator():
    def __init__(self, file_name, time_slice):
        self.os = OS(file_name, time_slice)

    def run(self):
        self.os.boot()
        while self.os.is_finished() is False:
            self.os.scheduler()



if __name__ == '__main__':
    try:
        sim = Simulator('input_file.txt', 2)
        #    -> cpu.start -> sim.os.boot()
        print('Start')
        sim.run()
        print('End')
        sim.os.print_queue("New")
        sim.os.put_in_ready_queue()
        sim.os.print_queue("Ready")
        #sim.os.scheduler()
        #sim.cpu.check_interrupt()
        #sim.os.print_queue("New")
        #while not sim.os.Ready_Queue.empty():
    except KeyboardInterrupt:
        sim.close()
        exit()






