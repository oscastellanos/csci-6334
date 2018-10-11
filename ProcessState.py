
from enum import Enum

class ProcessState(Enum):
    Ready = 0
    Running = 1
    Terminated = 2
    Waiting = 3