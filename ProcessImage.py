
from collections import namedtuple
from time import time

from PCB import PCB
from ProcessState import ProcessState

ProcessStatistics = namedtuple('ProcessStatistics', ['latency', 'response_times'])
    
class ProcessImage:
    def __init__(self, process_id, arrive_time, priority, program):
        self._PCB = PCB(process_id, arrive_time, priority, 0, ProcessState.New)
        self._program = program
        self._statistics = ProcessStatistics(None, tuple())
        self._program = program
        self.current_burst = self._program[0]
        self.creation_time = time()
        self.latency = None
        self.response_time = None
    
    def get_ID(self):
        return self._PCB.ID
        
    @property
    def priority(self):
        return self._PCB.priority
    
    def set_ready(self):
        if self._PCB.state == ProcessState.Waiting and self.response_time is None:
            self.response_time = time() - self.creation_time
        self._PCB = self._PCB._replace(state=ProcessState.Ready)

    def set_running(self):
        self._PCB = self._PCB._replace(state=ProcessState.Running)
        
    def set_terminated(self):
        self._PCB = self._PCB._replace(state=ProcessState.Terminated)
        self.latency = time() - self.creation_time
        
    def set_waiting(self):
        self._PCB = self._PCB._replace(state=ProcessState.Waiting)

    def next_instruction(self):
        if self._PCB.program_counter + 1 >= len(self._program):
            return None
        else:
            next_count = self._PCB.program_counter + 1
            self._PCB = self._PCB._replace(program_counter=next_count)
            burst = self._program[next_count]
            self.current_burst = burst
            self._PCB = self._PCB.set_next_instruction(next_count)
            return burst
            
    def set_instruction_length(self, length):
        self.current_burst = self.current_burst._replace(length=length)
        
    def get_current_burst(self):
        return self.current_burst
        
    def get_latency(self):
        return self.latency
        
    def get_response_time(self):
        return self.response_time