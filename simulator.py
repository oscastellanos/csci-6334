from OS import OS
from ProcessImage import ProcessImage
from collections import namedtuple
from ProcessState import ProcessState

from queue import Queue
import csv

PCB = namedtuple('PCB', ['ID', 'arrival', 'priority', 'program_counter',
                        'state'])

class Simulator():
    def __init__(self):
        self = self

    New_Queue = Queue()
    Ready_Queue = Queue()
    Wait_Queue = Queue()
    Terminated_Queue = Queue()

    def begin(self):
        with open('/home/osvaldo/Desktop/input_file.txt', 'r') as csvfile:
            processReader = csv.reader(csvfile)
            for row in processReader:
                process = PCB(int(row[0]), int(row[1]), int(row[2]), row[3], ProcessState.New.name)
                print(process.ID, process.arrival, process.priority, process.state)
                self.New_Queue.put(PCB)



    def ready(self):
        if self.New_Queue.empty():
            return -1
        else:
            gettingReady = self.New_Queue.get()
            #gettingReady.set_ready(1)
            self.Ready_Queue.put(gettingReady)

    # process from the Ready_Queue for CPU execution
    # Always check whether the CPU is idle or not; if yes, use your scheduler algorithm to select a
    # According to the return value of CPU execute(), put the process into the corresponding queue
    def run(self):
        if not self.cpu.isCPUbusy():
            process = self.Ready_Queue.get()
            process.set_running(1)
            self.cpu.execute(process)
            #self.cpu.setCPUIdle()


    def printReadyQueue(self):
        for process in list(self.Ready_Queue.queue):
            print(process.ID, process.state)



if __name__ == '__main__':
    test = Simulator()
    test.begin()
    test.ready()
    test.printReadyQueue()




