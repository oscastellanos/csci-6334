

from collections import deque
from Utils import work, ThreadedClass
from queue import Empty
from threading import main_thread, Event
from time import sleep

def task(N):
    for _ in range(N):
        work()
        
def handle_q(io_queue, ready_queue, event):
    while main_thread().is_alive():
        try:
            event.set()
            process = io_queue.get(False, 0.1)
            burst = process.get_current_burst()
            for _ in range(burst.get_length()):
                work()
            process.set_ready()
            process.next_instruction()
            ready_queue.put(process)
        except Empty:
            pass
        finally:
            event.clear()
            sleep(0.1)
        

class IODevice(ThreadedClass):
    def __init__(self, io_queue, ready_queue):
        self.io_queue = io_queue
        self.ready_queue = ready_queue
        self.current_task = None
        self.pcb = None
        self.event = Event()
        super().__init__()
    
    def start(self):
        self.task = super().submit(handle_q, self.io_queue, self.ready_queue,
                                    self.event)
    
    def submit(self, pcb):
        if self.current_task is None:
            self.pcb = pcb
            burst = pcb.get_next_instruction()
            self.current_task = super().submit(task, burst.get_length())
        else:
            self.deque.put(pcb)

    def is_finished(self):
        return not self.event.is_set()
            
    def join(self):
        self.event.wait()
            
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