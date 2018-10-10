
import heapq

from collections import deque, namedtuple


def get_round_robin(queue):
    '''Get an element from a list using round robin.'''
    return queue.pop(0)
    
def put_round_robin(queue, item):
    '''Put an element into a list using round robin.'''
    queue.append(item)
    
def get_priority_queue(queue):
    '''Get an element from a list using priority queue.
    
    Assumes that the elements in the queue are of the form:
    (priority, item)
    '''
    heapq.heapify(queue)
    return heapq.heappop(queue)[1]
    
def put_priority_queue(queue, priority, item):
    '''Put an element into a list using priority queue.'''
    prior_item = (priority, item)
    heapq.heapify(queue)
    heapq.heappush(queue, prior_item)
    

def test_functions():
    rr_list = [i for i in range(10)]
    print_str = []
    for _ in range(100):
        item = get_round_robin(rr_list)
        print_str.append(item)
        put_round_robin(rr_list, item)
    print_str = ', '.join([str(i) for i in print_str])
    print('Round Robin Func: ', print_str)
    
    pq_list = [(i, i) for i in range(10)]
    print_str = []
    for _ in range(100):
        item = get_priority_queue(pq_list)
        print_str.append(item)
        put_priority_queue(pq_list, item, item)
    print_str = ', '.join([str(i) for i in print_str])
    print('Priority Queue Func: ', print_str)
 
class RoundRobinQueue(deque):
    def __init__(self, maxlen=None):
        super().__init__(maxlen=maxlen)
        
    def get(self):
        return self.popleft()
        
    def put(self, item):
        self.append(item)

QueueItem = namedtuple('QueueItem', ['priority', 'item'])
        
class PriorityQueue(object):
    def __init__(self):
        self.queue = []
        
    def get(self):
        priority, item = heapq.heappop(self.queue)
        return item
        
    def put(self, item, priority):
        heapq.heappush(self.queue, QueueItem(priority, item))
        
def test_classes():
    rr_queue = RoundRobinQueue()
    for i in range(10):
        rr_queue.put(i)
    print_str = []
    for _ in range(100):
        item = rr_queue.get()
        print_str.append(item)
        rr_queue.put(item)
    print_str = ', '.join([str(i) for i in print_str])
    print('Round Robin Class: ', print_str)
    
    pq_queue = PriorityQueue()
    for i in range(10):
        pq_queue.put(i, i)
    print_str = []
    for _ in range(100):
        item = pq_queue.get()
        print_str.append(item)
        pq_queue.put(item, item)
    print_str = ', '.join([str(i) for i in print_str])
    print('Priority Queue Class: ', print_str)
 
if __name__ == '__main__':
    test_functions()
    test_classes()