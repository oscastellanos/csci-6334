
from collections import namedtuple
from itertools import accumulate

PCB = namedtuple('PCB', ['ID', 'arrival', 'priority', 'program_counter',
                        'state'])

ProcessStatistics = namedtuple('ProcessStatistics', ['latency', 'response_times'])
    
class ProcessImage:
    def __init__(self, process_id, arrive_time, priority, program):
        self._PCB = PCB(process_id, arrive_time, priority, 0, ProcessState.New)
        self._program = program
        # to do: other variables help you computing the latency, response, etc.
        self._statistics = ProcessStatistics(None, tuple())
        self._work_iterator = program

    def set_ready(self, time_slice):
        self._PCB = self._PCB._replace(state=ProcessState.Ready)

    def set_running(self, time_slice):
        self._PCB = self._PCB._replace(state=ProcessState.Running)
        
    def set_terminated(self, time_slice):
        self._PCB = self._PCB._replace(state=ProcessState.Terminated)

    def next_instruction(self):
        return next(self._work_iterator)