
# Producer-Consumer-Implementation
# producer showing

'##How it works 
This is a problem for the operating system where a consumer will consume files or resources in the memory that are still being produced or a producer will will produce files and add them to a buffer that is full. Now, the aim is to solve this problem by making sure that the producer does not add to a full buffer and it waits until the consumer has removed from the buffer to start producing again. Also the consumer should remove from the buffer if there are files or resources available but not to try and remove if there buffer is empty, which means the consumer should wait for the producer to produce and add file to the buffer for the consumer to start removing. 

Here we make use of the the semaphores empty, full and mutex to solve the problem.
##Empty: this semaphore is used to track the space in the buffer and this is set to the maximum size of the buffer and here we set the buffer size to 10.

##Full: initially set to 0 as the buffer is empty at the beginning. This semaphore is used to keep track of the number of available spaces in a buffer for the producer to fill.

##Mutex:this is used to control the access to the buffer such that only one process between the producer and consumer has access to the buffer. This has been initialized to 1. 

##The producer
Our producer generates student class and this class comprises of student information(student_ID, program and courses). This producer will produce student information randomly which comprises of the name, student_id, program, courses and marks obtained. This information will be fed into the buffer. The semaphore "empty" will indicate the buffer space available hence if it is full it will show so that the producer will stop producing until consumer has removed from the buffer. A producer process waiting in the empty() semaphore will beginning to produce when the value of the empty semaphore increases from 0 to 1 and so on to fill up the available spaces.

##The consumer
The consumer will be removing the student information that has been generated and added to the buffer by the producer. This will be consumed by consumer from the buffer and if there is non in the buffer then the consumer will wait until the producer has produced files before it can remove anything from the buffer. Everytime the consumer removes a file from the buffer the semaphore "full" will indicate the number of available files in the buffer. Everytime the consumer removes from the buffer, the empty() semaphore will increase from 0 to 1 and so on indicating that there's been space created.

##Technology used
This problem was solved using python programming language and coded on VScode. Python was selected because it's easier and it is a multi platform language.

##Future implementation
In the future we would like to incorporate security features. 

-.\env\Scripts\activate

- python main.py
