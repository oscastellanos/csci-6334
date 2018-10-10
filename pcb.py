# To do: PCB data structure of a process

# Process_id, Arrive_time, state,
# PositionOfNextInstructionToExecute(PC Value)

class PCB:
    PositionOfNextInstructionToExecute = 0

    def __init__(self, process_id, arrive_time, state, PositionOfNextInstructionToExecute):
        self.process_id = process_id
        self.arrive_time = arrive_time
        self.state = state
        self.PositionOfNextInstructionToExecute = PositionOfNextInstructionToExecute

    def setState(self, state):
        self.state = state

    def newToReady(self):
        self.state = "READY"

    def readyToRunning(self):
        self.state = "RUNNING"

    def next_instruction(self):


    def processImage():
