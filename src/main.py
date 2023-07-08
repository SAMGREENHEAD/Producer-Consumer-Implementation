import multiprocessing as mp
import threading
from producer import producer
from consumer import consumer
from buffer import buffer, buffer_full, buffer_empty, mutex
# Create and start the producer processes
# Create and start the producer processes
def start_producers(num_producers):
    producer_processes = []
    for i in range(num_producers):
        producer_process = mp.Process(target=producer, args=(i,))
        producer_processes.append(producer_process)
        producer_process.start()

    return producer_processes


# Create and start the consumer thread
def start_consumer():
    consumer_thread = threading.Thread(target=consumer)
    consumer_thread.start()
    return consumer_thread

if __name__ == '__main__':
    num_producers = 2  # Adjust the number of producers as needed

    producer_processes = start_producers(num_producers)
    consumer_thread = start_consumer()

    # Wait for all producer processes to finish
    for producer_process in producer_processes:
        producer_process.join()

    # Wait for the consumer thread to finish
    consumer_thread.join()
