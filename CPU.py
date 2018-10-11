

class CPU:
    PC = 1 # Your CPU only has one register PC
    mylist = [4, 5, 3, 2, 1, 4, 5, 6, 7, 8, 6, 5, 4, 3, 5, 6, 44, 5, 55, 433, 3]


    def __init__(self, timeslice):
        self.timeslice = timeslice
        self.BusyOrNot = False


    def isCPUbusy(self):
        return self.BusyOrNot

    def bubbleSort(self, mylist):
        sorted(self.mylist)

    def setCPUIdle(self):
        self.BusyOrNot = False

    def setCPUBusy(self):
        self.BusyOrNot = True

    def execute(self, process):
        self.setCPUBusy()
        for i in range(process.currentInstruction):
            sorted(self.mylist)



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