

from collections import deque
from Utils import work, ThreadedClass

def task(N):
    for _ in range(N):
        work()

class IOdevice(ThreadedClass):
    def __init__(self):
        self.queue = deque()
        self.current_task = None
        self.pcb = None
        super()
        
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