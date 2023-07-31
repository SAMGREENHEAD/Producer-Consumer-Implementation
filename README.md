# Producer-Consumer-Implementation# Producer-Consumer System with XML File Processing

This Python program processes student data and stores it in XML files using the producer-consumer design pattern. The system employs numerous producers to create random student data and write it to XML files, while a single consumer reads and processes the data from these files.

## Overview

In concurrent programming, the producer-consumer problem is a well-known synchronization issue. In this program, we implemented the producer-consumer pattern to show how multiple producers can efficiently generate data, and a consumer can process the data concurrently using a shared buffer to synchronize their interactions.

## Components

The program's components are as follows:

1.Producer: The producer creates arbitrary student data, transforms it to XML format, and then writes it to distinct XML files. To produce student data, several producer processes operate simultaneously.

2. Consumer: The consumer extracts student information from XML files, computes the average grade, and determines whether the student passed or failed. The consumer processes data simultaneously with the producers while running as a separate thread.

3. Buffer: The shared buffer is a Queue used to hold the file numbers (representing the XML files) produced by the producers. Semaphores are used to synchronize access to the buffer.

4. ITstudent Class: The `ITstudent` class represents a student with attributes like name, student ID, program, and a list of courses, each containing the name and mark of the course. The class includes methods to calculate the average marks and determine if the student has passed.

## How to Use

1. Ensure you have Python 3.x installed on your system.

2. Clone this repository to your local machine.

3. Install any required dependencies (if applicable) using `pip install <package_name>`.

4. Run the program by executing the `main.py` script. Adjust the number of producers and other settings as needed.

cd path/to/project/directory
python -m venv env
.\env\Scripts\activate
python main.py

5. Observe the console output to see how the producers generate data and write it to XML files, while the consumer reads and processes the data concurrently.

## Testing

A testing script, `test_producer_consumer.py`, is included in the repository to perform various tests on the producer-consumer system. The test script ensures that the system behaves correctly under different scenarios and configurations. To run the tests, execute `test_producer_consumer.py` and check the output for successful test results.

## Contributing

We welcome contributions to improve this program. If you find any issues or have suggestions for enhancements, feel free to open an issue or submit a pull request.

## License

This program is licensed under the MIT License - see the file for details.

## Acknowledgments

- This program is based on the classic producer-consumer problem in concurrent programming.
- Special thanks to the contributors for their efforts and ideas.
