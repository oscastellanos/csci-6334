class OS:
    #isCPUAvailable = True
    New_Queue = Queue()
    Ready_Queue = Queue()
    Wait_Queue = Queue()
    Terminated_Queue = Queue()
    ProcessTable = ProcessImage()
    cpu = CPU(10)

    #Processes = []

    # Read the txt input file, for each line, create a process and record its arrival time
    # Put each process in New_Queue initially, then put them in Ready_Queue
    def begin(self):
        with open('/home/osvaldo/Desktop/input_file.txt', 'r') as csvfile:
            processReader = csv.reader(csvfile)
            for row in processReader:
                processImage = ProcessImage(int(row[0]), int(row[1]), int(row[2]), row[3])
                self.New_Queue.put(processImage)

    '''def start_process(self):
        counter = 0
        for pcbid in self.Processes:
            self.Processes[counter] = ProcessImage(pcbid[0], pcbid[1], pcbid[2], pcbid[3])
            processImage = ProcessImage(self.Processes[counter])
            self.New_Queue.put(processImage)
            counter = counter + 1
'''
    def ready(self):
        if (self.New_Queue.empty()):
            return -1
        else:
            gettingReady = self.New_Queue.get()
            gettingReady.newToReady()
            self.Ready_Queue.put(gettingReady)

    # process from the Ready_Queue for CPU execution
    # Always check whether the CPU is idle or not; if yes, use your scheduler algorithm to select a
    # According to the return value of CPU execute(), put the process into the corresponding queue
    def run(self):
        if (not self.cpu.isCPUbusy()):
            process = self.Ready_Queue.get()
            process.readytoRunning()
            self.cpu.execute(process)
            #self.cpu.setCPUIdle()


    def printReadyQueue(self):
        for process in list(self.Ready_Queue.queue):
            print(process)




    # Record the time of every operation for computing your latency and response
    
def test_OS():
    operating_system = OS()
    operating_system.begin()
    operating_system.start_process()
    operating_system.ready()
    #operating_system.printReadyQueue()

if __name__ == '__main__':
    test_OS()