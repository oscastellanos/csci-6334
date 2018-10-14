from ProcessImage import ProcessImage
from ProcessState import ProcessState
from PCB import PCB
from CPU import CPU

from Utils import interpret

from queue import Queue
import csv


class OS:

    def __init__(self, file_name):
        # isCPUAvailable = True
        self.New_Queue = Queue()
        self.Ready_Queue = Queue()
        self.Wait_Queue = Queue()
        self.Terminated_Queue = Queue()
        self.file_name = file_name
        
        self.io = IODevice(self.Wait_Queue, self.Ready_Queue)
        self.io.start()

    def boot(self):
        with open(self.file_name, 'r') as csvfile:
            processReader = csv.reader(csvfile)

            for row in processReader:
                ID, arrival, priority, program = row
                ID = int(ID)
                arrival = int(arrival)
                priority = int(priority)
                program = interpret(program)
                process = ProcessImage(ID, arrival, priority, program)
                self.New_Queue.put(process)

    def put_in_ready_queue(self):
        if self.New_Queue.empty():
            return -1
        else:
            while not self.New_Queue.empty():
                gettingReady = self.New_Queue.get()
                ready = gettingReady.set_ready()
                self.Ready_Queue.put(ready)

    # process from the Ready_Queue for CPU execution
    # Always check whether the CPU is idle or not; if yes, use your scheduler algorithm to select a
    # According to the return value of CPU execute(), put the process into the corresponding queue

    def scheduler(self):
        if not self.cpu.isCPUbusy():
            process = self.Ready_Queue.get()
            process.set_running()
            remaining_time = self.cpu.execute(process)
            if remaining_time == 0:
                burst = process.next_instruction()
                if burst is None:
                    process.set_terminated()
                    self.Terminated_Queue.put(process)
                else:
                    process.set_waiting()
                    self.Wait_Queue.put(process)
            else:
                process.set_instruction_length(remaining_time)
                process.set_ready()

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
