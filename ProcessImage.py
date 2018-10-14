from ProcessState import ProcessState
from collections import namedtuple
from itertools import accumulate

PCB = namedtuple('PCB', ['ID', 'arrival', 'priority', 'program_counter',
                        'state'])

ProcessStatistics = namedtuple('ProcessStatistics', ['latency', 'response_times'])
    
class ProcessImage:
    def __init__(self, process_id, arrive_time, priority, program):
        self._PCB = PCB(process_id, arrive_time, priority, 0, ProcessState.New)
        self._program = program
        self._statistics = ProcessStatistics(None, tuple())
        self._program = program

    '''def __init__(self, PCB):
        self._PCB = PCB
        #self.PCB = PCB(process_id, arrive_time, priority, 0)
        # to do: other variables help you computing the latency, response, etc.
        self._statistics = ProcessStatistics(None, tuple())
        self._work_iterator = program
'''
    def set_ready(self, time_slice):
        self._PCB = self._PCB._replace(state=ProcessState.Ready)

    def set_running(self, time_slice):
        self._PCB = self._PCB._replace(state=ProcessState.Running)
        
    def set_terminated(self, time_slice):
        self._PCB = self._PCB._replace(state=ProcessState.Terminated)
        
    def set_waiting(self, time_slice):
        self._PCB = self._PCB._replace(state=ProcessState.Waiting)

    def next_instruction(self):
        if self._PCB.program_counter >= len(self._program):
            return None
        else
            next_count = self._PCB.program_counter
            self._PCB = self._PCB._replace(program_counter=next_count)
            burst = self.program[next_count]
            self.current_burst = burst
            self._PCB = self._PCB.set_next_instruction(burst)
            return burst
            
    def set_instruction_length(self, length):
        self.current_burst = self.current_burst._replace(length=length)
        
    def get_current_burst(self):
        return self.current_burst