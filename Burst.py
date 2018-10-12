
from collections import namedtuple
from enum import Enum

class BurstType(Enum):
    '''Used by Burst class to denote different types of Burst.'''
    CPU = 0
    IO = 1

class Burst(namedtuple('Burst', ['length', 'burst_type'])):
    __slots__ = ()
    def is_cpu_instruction(self):
        return self.burst_type == BurstType.CPU
        
    def is_io_instruction(self):
        return self.burst_type == BurstType.IO
        
    def get_length(self):
        return self.length
        