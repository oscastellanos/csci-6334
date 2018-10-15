from OS import OS
from ProcessImage import ProcessImage
from collections import namedtuple
from ProcessState import ProcessState
from CPU import CPU
from queue import Queue
import csv

from OS import OS


class Simulator():
    def __init__(self, file_name, time_slice):
        self.os = OS(file_name, time_slice)

    def run(self):
        self.os.boot()
        while self.os.is_finished() is False:
            self.os.scheduler()
            
    def close(self):
        self.os.close()



if __name__ == '__main__':
    try:
        sim = Simulator('input_file.txt', 2)
        #    -> cpu.start -> sim.os.boot()
        print('Start')
        sim.run()
        print('End')
        Q = []
        while not sim.os.Terminated_Queue.empty():
            Q.append(sim.os.Terminated_Queue.get())
        for proc in Q:
            print(proc.get_ID(), proc.get_latency(), proc.get_response_time())
        
    except KeyboardInterrupt:
        sim.close()
        exit()






