from ProcessImage import ProcessImage
from ProcessState import ProcessState
from PCB import PCB
from CPU import CPU

from queue import Queue
import csv


class OS:
    # isCPUAvailable = True
    New_Queue = Queue()
    Ready_Queue = Queue()
    Wait_Queue = Queue()
    Terminated_Queue = Queue()

    def boot(self):
        with open('/home/osvaldo/Desktop/input_file.txt', 'r') as csvfile:
            processReader = csv.reader(csvfile)

            for row in processReader:
                process = PCB(int(row[0]), int(row[1]), int(row[2]), row[3], ProcessState.New.name)
                #print(process.ID, process.arrival, process.priority, process.program_counter, process.state)
                self.New_Queue.put(process)



    def put_in_ready_queue(self):
        if self.New_Queue.empty():
            return -1
        else:
            while not self.New_Queue.empty():
                gettingReady = self.New_Queue.get()
                ready = gettingReady.update_state(ProcessState.Ready.name)
                self.Ready_Queue.put(ready)

    # process from the Ready_Queue for CPU execution
    # Always check whether the CPU is idle or not; if yes, use your scheduler algorithm to select a
    # According to the return value of CPU execute(), put the process into the corresponding queue

    def scheduler(self):
        if not self.cpu.isCPUbusy():
            process = self.Ready_Queue.get()
            process.set_running()
            self.cpu.execute(process)
            # self.cpu.setCPUIdle()

    def printReadyQueue(self):
        for process in list(self.Ready_Queue.queue):
            print(process)

    def print_queue(self, queue):
        if queue == "New":
            for process in list(self.New_Queue.queue):
                print(process.ID, process.arrival, process.priority, process.program_counter, process.state)
        if queue == "Ready":
            for process in list(self.Ready_Queue.queue):
                print(process.ID, process.arrival, process.priority, process.program_counter, process.state)
        if queue == "Wait":
            for process in list(self.Wait_Queue.queue):
                print(process.ID, process.arrival, process.priority, process.program_counter, process.state)
        if queue == "Terminated":
            for process in list(self.Terminated_Queue.queue):
                print(process.ID, process.arrival, process.priority, process.program_counter, process.state)

    # Record the time of every operation for computing your latency and response
