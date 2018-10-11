#import numpy as np
import csv
import scheduler
from queue import Queue


class PCB:
    # Process_id, Arrive_time, state,
    # PositionOfNextInstructionToExecute(PC Value)


    def __init__(self, process_id, arrive_time, priority, PositionOfNextInstructionToExecute):
        self.process_id = process_id
        self.arrival_time = arrive_time
        self.priority = priority
        self.PositionOfNextInstructionToExecute = PositionOfNextInstructionToExecute
        self.state = "NEW"

class ProcessImage:
    Process_ids = [[]]
    CPU_IOBurstSequence = ""

    def __init__(self):
        self.CPU_IOBurstSequence = CPU_IOBURSTSequence
        self.currentInstructionIndex = 0
        self.nextInstructionIndex = self.currentInstructionIndex + 1
        self.currentInstruction = CPU_IOBURSTSequence[self.currentInstructionIndex]
        self.PCB = PCB(process_id, arrive_time, priority, self.CPU_IOBurstSequence[self.nextInstructionIndex])
        self.numOfInstructions = len(CPU_IOBURSTSequence)
    # to do: other variables help you computing the latency, response, etc.


    def Process(self, process_id, arrive_time, priority, CPU_IOBURSTSequence):
        self.Process_ids.append([process_id, PCB(process_id, arrive_time, priority, )])

    def setState(self, state):
        self.PCB.state = state

    def newToReady(self):
        self.PCB.state = "READY"

    def readyToRunning(self):
        self.PCB.state = "RUNNING"

    def next_instruction(self):
        if ( self.nextInstructionIndex < self.numOfInstructions):
            self.PCB.PositionOfNextInstructionToExecute = self.CPU_IOBurstSequence[self.nextInstructionIndex]

        else:
            return "terminated"




class CPU:
    PC = 1 # Your CPU only has one register PC
    mylist = [4, 5, 3, 2, 1, 4, 5, 6, 7, 8, 6, 5, 4, 3, 5, 6, 44, 5, 55, 433, 3]


    def __init__(self, timeslice):
        self.timeslice = timeslice
        self.BusyOrNot = False


    def isCPUbusy(self):
        return self.BusyOrNot

    def bubbleSort(self, mylist):
        sorted(self.mylist)

    def setCPUIdle(self):
        self.BusyOrNot = False

    def setCPUBusy(self):
        self.BusyOrNot = True

    def execute(self, process):
        self.setCPUBusy()
        for i in range(process.currentInstruction):
            sorted(self.mylist)



    '''
    Read the CPU burst number (# from PositionOfNext...)
    Repeat calling bubblesort for # of times and continue
    
    case: code runs out, return positionofnext, "terminated", 
    then OS put it back to the terminated queue.
    
    case: if the slice of time (restricted number of calling bubblesort for a
    process each time) runs out, return (PositionOf..+1, "ready"), then OS puts it back
    to the ready queue.
    
    otherwise: return(PositionOfNext..+1, "wait")
    (namely, P has an I/O request and then OS removes it from the ready queue
    and sends it to the I/O queue
    '''

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
    ProcessTable = ProcessImage()
    cpu = CPU(10)

    #Processes = []

    # Read the txt input file, for each line, create a process and record its arrival time
    # Put each process in New_Queue initially, then put them in Ready_Queue
    def begin(self):
        with open('/home/osvaldo/Desktop/input_file.txt', 'r') as csvfile:
            processReader = csv.reader(csvfile)
            for row in processReader:
                processImage = ProcessImage(int(row[0]), int(row[1]), int(row[2]), row[3])
                self.New_Queue.put(processImage)

    '''def start_process(self):
        counter = 0
        for pcbid in self.Processes:
            self.Processes[counter] = ProcessImage(pcbid[0], pcbid[1], pcbid[2], pcbid[3])
            processImage = ProcessImage(self.Processes[counter])
            self.New_Queue.put(processImage)
            counter = counter + 1
'''
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
            self.cpu.execute(process)
            #self.cpu.setCPUIdle()


    def printReadyQueue(self):
        for process in list(self.Ready_Queue.queue):
            print(process)




    # Record the time of every operation for computing your latency and response


def test_OS():
    operating_system = OS()
    operating_system.begin()
    operating_system.start_process()
    operating_system.ready()
    #operating_system.printReadyQueue()

if __name__ == '__main__':
    test_OS()