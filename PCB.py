

class PCB:
    # Process_id, Arrive_time, state,
    # PositionOfNextInstructionToExecute(PC Value)


    def __init__(self, process_id, arrive_time, priority, PositionOfNextInstructionToExecute):
        self.process_id = process_id
        self.arrival_time = arrive_time
        self.priority = priority
        self.PositionOfNextInstructionToExecute = PositionOfNextInstructionToExecute
        self.state = "NEW"