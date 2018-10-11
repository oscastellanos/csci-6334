
from enum import Enum

class ProcessState(Enum):
    Ready = 0
    Running = 1
    Terminated = 2
    New = 3
    Waiting = 4