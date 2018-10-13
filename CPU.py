from collections import deque
from Utils import work, ThreadedClass

class CPU(ThreadedClass):
    PC = 1 # Your CPU only has one register PC


    def __init__(self, timeslice):
        self.timeslice = timeslice
        self.BusyOrNot = False
        self.current_task = None
        super()


    def isCPUbusy(self):
        return self.BusyOrNot


    def setCPUIdle(self):
        self.BusyOrNot = False

    def setCPUBusy(self):
        self.BusyOrNot = True

    def execute(self, process):
        self.setCPUBusy()
        for i in range(process.currentInstruction):
            sorted(self.mylist)

    def submit(self, pcb):
        if self.current_task is None:
            self.pcb = pcb
            burst = pcb.get_next_instruction()
            self.current_task = super().submit(task, burst.get_length())
        else:
            self.deque.append(pcb)

    # Always pick one process from the Wait_Queue to execute

    def check_interrupt(self):
        if self.current_task is None:
            return False
        elif self.current_task.done():
            finished_pcb = self.pcb
            self.current_task = None
            pcb = deque.popleft()
            self.submit(pcb)
            return finished_pcb
        else:
            return False



    '''
    Read the CPU burst number (# from PositionOfNext...)
    Repeat calling bubblesort for # of times and continue
    
    case: code runs out, return positionofnext, "terminated", 
    then OS put it back to the terminated queue.
    
    case: if the slice of time (restricted number of calling bubblesort for a
    process each time) runs out, return (PositionOf..+1, "ready"), then OS puts it back
    to the ready queue.
    
    otherwise: return(PositionOfNext..+1, "wait")
    (namely, P has an I/O request and then OS removes it from the ready queue
    and sends it to the I/O queue
    '''