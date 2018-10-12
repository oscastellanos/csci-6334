
from collections import namedtuple

from ProcessState import ProcessState


PCB = namedtuple('PCB', ['ID', 'arrival', 'priority', 'program_counter',
                        'state'])

class PCB:
    def __init__(self, process_id, arrive_time, priority, PositionOfNextInstructionToExecute):
        self.process_id = process_id
        self.arrival_time = arrive_time
        self.priority = priority
        self.PositionOfNextInstructionToExecute = PositionOfNextInstructionToExecute
        self.state = ProcessState.new