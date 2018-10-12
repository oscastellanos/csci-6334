
from Utils import work

from 
    

class IOdevice(object):
    # Public IOdevice(ArrayList<Process> Wait_Queue)

    # public boolean BusyOrNot

    def __init__(self, Wait_Queue):
        self.Wait_Queue = Wait_Queue



    def bubbleSort(self):
        work()

    # Always pick one process from the Wait_Queue to execute

    def execute(self, IO_Burst):
        # BusyOrNot = true
        # call bubble sort() for IO_Burst times and then return "ready"
        for _ in range(IO_Burst):
            work()

        return "ready" 