from queue import Queue
from threading import Semaphore

# Define the maximum buffer size
MAX_BUFFER_SIZE = 10

# Create a queue for the shared buffer
buffer = Queue(MAX_BUFFER_SIZE)

# Create semaphores for synchronization
buffer_full = Semaphore(0)
buffer_empty = buffer_empty = Semaphore(MAX_BUFFER_SIZE - buffer.qsize()) 
mutex = Semaphore(1)
