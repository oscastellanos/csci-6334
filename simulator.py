from OS import OS
from ProcessImage import ProcessImage
from collections import namedtuple
from ProcessState import ProcessState
from CPU import CPU
from queue import Queue
import csv

PCB = namedtuple('PCB', ['ID', 'arrival', 'priority', 'program_counter',
                         'state'])


class Simulator():
    cpu = CPU(3)
    os = OS()

    New_Queue = Queue()
    Ready_Queue = Queue()
    Wait_Queue = Queue()
    Terminated_Queue = Queue()

    def __init__(self):
        self = self

    def run(self):
        self.cpu.start(self.os)
        self.cpu.setCPUBusy()



if __name__ == '__main__':
    sim = Simulator()
    #    -> cpu.start -> sim.os.boot()
    sim.run()
    sim.os.print_queue("New")
    sim.os.put_in_ready_queue()
    sim.os.print_queue("Ready")
    #sim.os.scheduler()
    #sim.cpu.check_interrupt()
    #sim.os.print_queue("New")
    #while not sim.os.Ready_Queue.empty():






