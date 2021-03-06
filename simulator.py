import numpy as np

from OS import create_OS_FCFS, create_OS_RR, create_OS_Priority


class Simulator():
    def __init__(self, os_object):
        self.os = os_object

    def run(self):
        self.os.boot()
        while self.os.is_finished() is False:
            self.os.scheduler()
            
    def close(self):
        self.os.close()

def compute_measurements(X):
    avg = np.mean(latencies)
    std = np.std(latencies)
    mini = np.min(latencies)
    maxi = np.max(latencies)
    return avg, std, mini, maxi
        
if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    args = parser.parse_args()

    fcfs = create_OS_FCFS(args.file_name, 2)
    rr = create_OS_RR(args.file_name, 2)
    priority = create_OS_Priority(args.file_name, 2)
    
    for os_object in [fcfs, rr, priority]:
        print('\nCurrent OS: ', os_object)
        sim = Simulator(os_object)
        sim.run()
        throughput = sim.os.get_throughput()
        Q = []
        while not sim.os.Terminated_Queue.empty():
            Q.append(sim.os.Terminated_Queue.get())
        latencies = [proc.get_latency() for proc in Q]
        response_times = [proc.get_response_time() for proc in Q]
        
        for proc in Q:
            print(proc.get_ID(), proc.get_latency(), proc.get_response_time())
            
        avg, std, mini, maxi = compute_measurements(latencies)
        print('Latency (Avg, Std): {:2.3f} +- {:2.3f} secs'.format(avg, std))
        print('Latency Min: {:2.3f} Max: {:2.3f} secs'.format(mini, maxi))
        avg, std, mini, maxi = compute_measurements(response_times)
        print('Response Time (Avg, Std): {:2.3f} +- {:2.3f} secs'.format(avg, std))
        print('Response Time Min: {:2.3f} Max: {:2.3f} secs'.format(mini, maxi))
        print('OS Throughput: ', throughput)






