from collections import namedtuple
from ProcessState import ProcessState

from ProcessState import ProcessState

PCB = namedtuple('PCB', ['ID', 'arrival', 'priority', 'program_counter',
                         'state'])



class PCB(PCB):
    __slots__ = ()

    def get_ID(self):
        return self.ID

    def update_state(self, new_state):
        return self._replace(state=new_state)

    def set_next_instruction(self, next_instruction):
        return self._replace(program_counter=next_instruction)

    def get_next_instruction(self):
        return self.program_counter