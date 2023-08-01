
## Producer-Consumer-Implementation# Producer-Consumer System with XML File Processing
This Python program processes student data and stores it in XML files using the producer-consumer design pattern. The system employs numerous producers to create random student data and write it to XML files, while a single consumer reads and processes the data from these files.

## How it works 
This is a problem for the operating system where a consumer will consume files or resources in the memory that are still being produced or a producer will will produce files and add them to a buffer that is full. Now, the aim is to solve this problem by making sure that the producer does not add to a full buffer and it waits until the consumer has removed from the buffer to start producing again. Also the consumer should remove from the buffer if there are files or resources available but not to try and remove if there buffer is empty, which means the consumer should wait for the producer to produce and add file to the buffer for the consumer to start removing. 

Here we make use of the the semaphores empty, full and mutex to solve the problem.
## Empty: this semaphore is used to track the space in the buffer and this is set to the maximum size of the buffer and here we set the buffer size to 10.

## Full: initially set to 0 as the buffer is empty at the beginning. This semaphore is used to keep track of the number of available spaces in a buffer for the producer to fill.

## Mutex:this is used to control the access to the buffer such that only one process between the producer and consumer has access to the buffer. This has been initialized to 1. 

## Setting Up the Environment**:
The program starts by importing necessary libraries, such as `multiprocessing`, `threading`, and `xml.etree.ElementTree`. The shared buffer and semaphores for synchronization are defined. The `ITstudent` class is created with methods to calculate the average mark and check if a student has passed. Functions are defined to generate random student data and convert student objects to XML strings.

The program's components are as follows:

## The producer
The producer process is a separate process that runs independently from the main thread. It generates random student data and converts it to an XML format using the provided functions. Our producer generates student class and this class comprises of student information(student_ID, program and courses). The producer creates arbitrary student data, transforms it to XML format, and then writes it to distinct XML files. It then puts the file number (an integer representing the student file) in the buffer and writes the corresponding XML data to a file with a unique filename. After writing the XML data, the producer releases the `mutex` to allow other processes to access the buffer and increments the `buffer_full` semaphore to signal the consumer that a new file is available for processing. To produce student data, several producer processes operate simultaneously. This information will be fed into the buffer. The semaphore "empty" will indicate the buffer space available hence if it is full it will show so that the producer will stop producing until consumer has removed from the buffer. A producer process waiting in the empty() semaphore will beginning to produce when the value of the empty semaphore increases from 0 to 1 and so on to fill up the available spaces. This process is repeated for a few students until the producer puts the `END_OF_FILES` constant in the buffer to signal the end of data production.


## The consumer
The consumer thread runs as a separate thread within the main process. It starts by acquiring the `buffer_full` semaphore to wait for the producer to put data in the buffer.Upon acquiring the `buffer_full` semaphore, the consumer acquires the `mutex` to get exclusive access to the buffer and begins processing data. The consumer first checks the buffer contents. If the buffer is empty (no data produced yet), it releases the `mutex` and the `buffer_empty` semaphore to signal the producer to produce more data. If the consumer receives the `END_OF_FILES` signal from the producer, it exits the loop, releases the `mutex`, and the `buffer_empty` semaphore to signal the producer to finish. Otherwise, it consumes the file number from the buffer, releases the `mutex`, decrements the `buffer_full` semaphore to indicate a slot is consumed, and processes the corresponding XML file. After processing the XML file, the consumer prints the student's information (name, ID, program, courses, average, pass/fail), deletes the XML file, and continues to the next iteration of the loop.
The consumer processes data simultaneously with the producers while running as a separate thread. This will be consumed by consumer from the buffer and if there is non in the buffer then the consumer will wait until the producer has produced files before it can remove anything from the buffer. Everytime the consumer removes a file from the buffer the semaphore "full" will indicate the number of available files in the buffer. Everytime the consumer removes from the buffer, the empty() semaphore will increase from 0 to 1 and so on indicating that there's been space created.

## Main Script:
  The main script starts by defining the number of producer processes (currently set to 1) and creating the corresponding producer processes. Each producer process runs independently, generating random student data and adding it to the shared buffer. The main script also creates the consumer thread, which processes the data from the buffer when it becomes available. The main script waits for all producer processes to finish their tasks using `join()` to ensure all data is produced before setting the event to signal the consumer thread to finish. After the producer processes finish, the main script sets the event to signal the consumer thread to stop processing. Finally, the main script waits for the consumer thread to finish using `join()` before ending the program.

## Buffer
The shared buffer is a Queue used to hold the file numbers (representing the XML files) produced by the producers. Semaphores are used to synchronize access to the buffer.

## ITstudent Class
The `ITstudent` class represents a student with attributes like name, student ID, program, and a list of courses, each containing the name and mark of the course. The class includes methods to calculate the average marks and determine if the student has passed.

## How to Use

1. Ensure you have Python 3.x installed on your system.

2. Clone this repository to your local machine.

3. Install any required dependencies (if applicable) using `pip install <package_name>`.

4. Run the program by executing the `main.py` script. Adjust the number of producers and other settings as needed.

cd path/to/project/directory
python -m venv env
-.\env\Scripts\activate
- python main.py

5. Observe the console output to see how the producers generate data and write it to XML files, while the consumer reads and processes the data concurrently.

## Issues Detected and Debugging Attempts:
1. The initial issue was that the consumer thread was not consuming data from the buffer. This could have been due to synchronization problems between the producer and consumer.
2. Additional print statements were added to the producer and consumer code to understand their behavior and check the status of the semaphores and buffer.
3. It was confirmed that the producer was correctly releasing the `buffer_full` semaphore after adding data to the buffer.
4. The consumer, however, was still not consuming data even though it correctly acquired the `buffer_full` semaphore and the `mutex`. The issue seemed to be related to the `buffer_empty` semaphore not being released correctly by the consumer, which affected the producer's ability to produce more data.

## solutions
An issue that we managed to solve was that of concurrency.

## Technology used
This problem was solved using python programming language and coded on VScode. Python was selected because it's easier and it is a multi platform language.

## Contributing
We welcome contributions to improve this program. If you find any issues or have suggestions for enhancements, feel free to open an issue or submit a pull request.

## Future implementation
In the future we would like to incorporate security features and resolve. 

## License

This program is licensed under the MIT License - see the file for details.

## Acknowledgments

- This program is based on the classic producer-consumer problem in concurrent programming.
- Special thanks to the contributors for their efforts and ideas.
