import ProcessImg
import pcb
#import numpy as np
import csv

class OS:

    # public CPU cpu
    # public IOdevice io
    # public boolean isCPUAvailable
    isCPUAvailable = True
    # public ProcessTable process_table
    # ArrayList<Process> New_Queue
    New_Queue = []
    # ArrayList<Process> Ready_Queue
    Ready_Queue = []
    # ArrayList<Process> Wait_Queue
    Wait_Queue = []
    # ArrayList<Process> Terminated_Queue
    Terminated_Queue = []

    Processes = []



    # Read the txt input file, for each line, create a process and record its arrival time
    # Put each process in New_Queue initially, then put them in Ready_Queue
    def read_input(self):
        with open('/home/osvaldo/Desktop/input_file.txt', 'r') as csvfile:
            processReader = csv.reader(csvfile)
            for row in processReader:
                self.New_Queue.append(row[0])
                self.Processes.append([row[0], row[1], row[2], row[3]])


    def start_process(self):
        self = self
        for pcbid in self.Processes:
            self.Processes[pcbid[0]] = pcb(pcbid[0], pcbid[1], pcbid[2], pcbid[3])



    # process from the Ready_Queue for CPU execution
    # Always check whether the CPU is idle or not; if yes, use your scheduler algorithm to select a
    # According to the return value of CPU execute(), put the process into the corresponding queue


    # Record the time of every operation for computing your latency and response

    def average(self):
        self = self

    #def minimum(self):

    #def maximum(self):

    #def standard_deviation(self):

    #def priority(self):

    #def latency(self):

    #def responseTime(self):

    #def throughput(self):

    #def FCFS(self):

