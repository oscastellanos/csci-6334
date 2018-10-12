import numpy as np

from collections import namedtuple
from abc import ABC, abstractmethod

from Burst import Burst


def interpret(code_sequence):
    burst_types = itertools.cycle([BurstType.CPU, BurstType.IO])
    return [Burst(l, bt) for l, bt in zip(code_sequence, burst_types)]

def work(N=2**10):
    A = np.random.choice(range(N), N, replace=False)
    bubble_sort(A)

def bubble_sort(A):
    N = len(A)
    B = np.sum(A < np.expand_dims(A, -1), axis=0)
    C = np.empty(N)
    C[B] = A[range(N)]
    return C
    
def create_work_schedule(sequence):
    for i, slice in enumerate(sequence):
        if i%2 == 0:
            yield (OSOps.CPU, slice)
        else:
            yield (OSOps.IO, slice)