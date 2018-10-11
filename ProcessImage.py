
from collections import namedtuple
import ProcessState

ProcessStatistics = namedtuple('ProcessStatistics', ['latency', 'response_times'])
    
class ProcessImage:
    def __init__(self, PCB):
        self._PCB = PCB
        #self.PCB = PCB(process_id, arrive_time, priority, 0)
        # to do: other variables help you computing the latency, response, etc.
        self._statistics = ProcessStatistics(None, tuple())
        
    def setState(self, state):
        if state in ProcessState:
            self.PCB.state = state
            return True
        else:
            return False

    def set_ready(self, time_slice):
        self.PCB.state = ProcessState.Ready

    def set_running(self, time_slice):
        self.PCB.state = ProcessState.Running
        
    def set_terminated(self, time_slice):
        self.PCB.state = ProcessState.Terminated

    def next_instruction(self):
        return self._PCB.PositionOfNextInstructionToExecute