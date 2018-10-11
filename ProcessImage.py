
from collections import namedtuple

ProcessStatistics = namedtuple('ProcessStatistics', ['latency', 'response_times'])
    
class ProcessImage:
    CPU_IOBurstSequence = ""

    def __init__(self, PCB):
        self._PCB = PCB
        self.PCB = PCB(process_id, arrive_time, priority, 0)
        # to do: other variables help you computing the latency, response, etc.
        self._statistics = ProcessStatistics(None, tuple())
        
    def setState(self, state):
        if state in ProcessState:
            self.PCB.state = state
            return True
        else:
            return False

    def newToReady(self):
        self.PCB.state = ProcessState.Ready

    def readyToRunning(self):
        self.PCB.state = ProcessState.Running

    def next_instruction(self):
        return self._PCB.PositionOfNextInstructionToExecute