from time import time
from enum import Enum

from ProcessImage import ProcessImage
from ProcessState import ProcessState
from PCB import PCB
from CPU import CPU

from Utils import interpret

from queue import Queue
import csv

from IODevice import IODevice
from ProcessImage import ProcessImage
from CPU import CPU

from scheduler import RoundRobinQueue, PriorityQueue

class SchedulerType(Enum):
    FCFS = 0
    RR = 1
    Priority = 2

def create_OS_FCFS(file_name, time_slice):
    return OS(file_name, time_slice, SchedulerType.FCFS)
    
def create_OS_RR(file_name, time_slice):
    return OS(file_name, time_slice, SchedulerType.RR)
    
def create_OS_Priority(file_name, time_slice):
    return OS(file_name, time_slice, SchedulerType.Priority)

class OS(object):

    def __init__(self, file_name, time_slice, scheduler_type):
        self.New_Queue = Queue()
        self.scheduler_type = scheduler_type
        if scheduler_type is SchedulerType.FCFS:
            self.Ready_Queue = Queue()
        elif scheduler_type is SchedulerType.RR:
            self.Ready_Queue = RoundRobinQueue()
        elif scheduler_type is SchedulerType.Priority:
            self.Ready_Queue = PriorityQueue()
        self.Wait_Queue = Queue()
        self.Terminated_Queue = Queue()
        self.file_name = file_name
        self.os_start = None
        self.number_of_processes = 0
        self.time_slice = time_slice
        
        self.io = None
        self.cpu = None
        
    def __str__(self):
        if self.scheduler_type is SchedulerType.FCFS:
            return 'Class OS with Scheduler: FCFS'
        elif self.scheduler_type is SchedulerType.RR:
            return 'Class OS with Scheduler: RR'
        elif self.scheduler_type is SchedulerType.Priority:
            return 'Class OS with Scheduler: Priority'
        
    def is_finished(self):
        return self.New_Queue.empty() and self.Ready_Queue.empty() and self.Wait_Queue.empty() and self.io.is_finished() and not self.cpu.isCPUbusy()

    def boot(self):
        self.os_start = time()
        self.number_of_processes = 0
        
        self.io = IODevice(self.Wait_Queue, self.Ready_Queue)
        self.io.start()
        
        self.cpu = CPU(self.time_slice)
        with open(self.file_name, 'r') as csvfile:
            processReader = csv.reader(csvfile)

            for row in processReader:
                ID, arrival, priority, program = row
                ID = int(ID)
                arrival = int(arrival)
                priority = int(priority)
                program = program.strip().strip(';')
                program = [int(i) for i in program]
                program = interpret(program)
                process = ProcessImage(ID, arrival, priority, program)
                self.New_Queue.put(process)
                self.number_of_processes += 1
        self.put_in_ready_queue()

    def put_in_ready_queue(self):
        if self.New_Queue.empty():
            return -1
        else:
            while not self.New_Queue.empty():
                gettingReady = self.New_Queue.get()
                gettingReady.set_ready()
                self.Ready_Queue.put(gettingReady)

    # process from the Ready_Queue for CPU execution
    # Always check whether the CPU is idle or not; if yes, use your scheduler algorithm to select a
    # According to the return value of CPU execute(), put the process into the corresponding queue

    def scheduler(self):
        if not self.cpu.isCPUbusy():
            process = self.Ready_Queue.get()
        else:
            process = self.current_process
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
            if isinstance(self.Ready_Queue, RoundRobinQueue):
                self.current_process = None
                process.set_ready()
                self.Ready_Queue.put(process)
            else:
                self.current_process = process
                self.cpu.setCPUBusy()
            

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
    def close(self):
        self.io.join()
        self.io.close()
        
    def get_throughput(self):
        return self.number_of_processes/(time() - self.os_start)