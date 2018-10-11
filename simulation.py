#import numpy as np
import csv
import scheduler
from queue import Queue


# To do: PCB data structure of a process

# Process_id, Arrive_time, state,
# PositionOfNextInstructionToExecute(PC Value)

class PCB:
    PositionOfNextInstructionToExecute = 0
    state = "NEW"


    def __init__(self, process_id, arrive_time, state, PositionOfNextInstructionToExecute):
        self.process_id = process_id
        self.arrive_time = arrive_time
        self.state = state
        self.PositionOfNextInstructionToExecute = PositionOfNextInstructionToExecute

    def setState(self, state):
        self.state = state

    def newToReady(self):
        self.state = "READY"

    def readyToRunning(self):
        self.state = "RUNNING"

    def next_instruction(self):
        self = self

    #def processImage():
    #    self = self


class ProcessImage:
    CPU_IOBurstSequence = ' '
    def __init__(self, PCB):
        self.PCB = PCB
    #global code = CPU-I/O burst Sequence;
    # to do: other variables help you computing the latency, response, etc.



    def Process(self, PCB):
        self = self
        # set PCB data, code and others
        # set state as "NEW"



class CPU:

    BusyOrNot = False
    PC = 1 # Your CPU only has one register PC
    timeslice = 0
    PositionOfNextInstructionToExecute = 1
    mylist = [4, 5, 3, 2, 1, 4, 5, 6, 7, 8, 6, 5, 4, 3, 5, 6, 44, 5, 55, 433, 3]


    def __init__(self, timeslice):
        self.timeslice = timeslice
        #self.BusyOrNot = BusyOrNot
        #self.PC = PC
        #self.PositionOfNextInstructionToExecute = PositionOfNextInstructionToExecute


    def isCPUbusy(self):
        return self.BusyOrNot

    def bubbleSort(self, mylist):
        sorted(self.mylist)

    def setCPUIdle(self):
        self.BusyOrNot = False

    def setCPUBusy(self):
        self.BusyOrNot = True

    def execute(self, process):
        for i in range(4):
            sorted(self.mylist)


class IOdevice:
    # Public IOdevice(ArrayList<Process> Wait_Queue)

    # public boolean BusyOrNot

    def __init__(self, Wait_Queue):
        self.Wait_Queue = Wait_Queue



    def bubbleSort(self):
        self = self

    # Always pick one process from the Wait_Queue to execute

    def execute(self, IO_Burst):
        # BusyOrNot = true
        # call buble sort() for IO_Burst times and then return "ready"
        for i in range(IO_Burst):
            sorted()

        return("ready")


class OS:
    #isCPUAvailable = True
    New_Queue = Queue()
    Ready_Queue = Queue()
    Wait_Queue = Queue()
    Terminated_Queue = Queue()
    cpu = CPU(10)

    Processes = []

    # Read the txt input file, for each line, create a process and record its arrival time
    # Put each process in New_Queue initially, then put them in Ready_Queue
    def read_input(self):
        with open('/home/osvaldo/Desktop/input_file.txt', 'r') as csvfile:
            processReader = csv.reader(csvfile)
            for row in processReader:
                self.Processes.append([row[0], row[1], row[2], row[3]])


    def start_process(self):
        self = self
        counter = 0
        for pcbid in self.Processes:
            self.Processes[counter] = PCB(pcbid[0], pcbid[1], pcbid[2], pcbid[3])
            self.New_Queue.put(self.Processes[counter])
            counter = counter + 1

    def ready(self):
        if (self.New_Queue.empty()):
            return -1
        else:
            gettingReady = self.New_Queue.get()
            gettingReady.newToReady()
            self.Ready_Queue.put(gettingReady)

    # process from the Ready_Queue for CPU execution
    # Always check whether the CPU is idle or not; if yes, use your scheduler algorithm to select a
    # According to the return value of CPU execute(), put the process into the corresponding queue
    def run(self):
        if (not self.cpu.isCPUbusy()):
            process = self.Ready_Queue.get()
            process.readytoRunning()
            self.cpu.setCPUBusy()
            self.cpu.execute(process)
            self.cpu.setCPUIdle()

    def printReadyQueue(self):
        for process in list(self.Ready_Queue.queue):
            print(process)




    # Record the time of every operation for computing your latency and response


def test_OS():
    operating_system = OS()
    operating_system.read_input()
    operating_system.start_process()
    operating_system.ready()
    #operating_system.printReadyQueue()

if __name__ == '__main__':
    test_OS()