import threading
from student import ITstudent
import xml.etree.ElementTree as ET
from buffer import buffer, buffer_full, buffer_empty, mutex

END_OF_FILES = -1

# Convert XML file to student object
def xml_to_student(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    name = root.find('name').text
    student_id = root.find('id').text
    program = root.find('program').text

    courses = []
    for course_element in root.find('courses'):
        course_name = course_element.find('name').text
        mark = int(course_element.find('mark').text)
        courses.append({'name': course_name, 'mark': mark})

    return ITstudent(name, student_id, program, courses)

# Delete XML file
def delete_xml_file(filename):
    import os
    os.remove(filename)

# Consumer function with event argument
def consumer(event):
    print("Consumer thread started")
    items_in_buffer = 0

    while not event.is_set():
        buffer_full.acquire()  # Wait for a filled slot in the buffer
        print("Consumer acquired buffer_full semaphore")
        mutex.acquire()  # Acquire exclusive access to the buffer

        # Print buffer size and contents for debugging
        print(f"Buffer size before acquiring: {buffer.qsize()}, Contents: {list(buffer.queue)}")

        # Check if the buffer is empty before accessing the first item
        if items_in_buffer == 0:
            mutex.release()  # Release mutex if buffer is empty
            print("Consumer released mutex (buffer empty)")
            continue

        if buffer.queue[0] == END_OF_FILES:
            buffer.get()  # Remove the END_OF_FILES constant from the buffer
            print("Consumer received END_OF_FILES. Exiting loop.")
            mutex.release()  # Release mutex before exiting the loop
            break

      # Decrement the items_in_buffer counter and get the file number from the buffer
        items_in_buffer -= 1
        file_number = buffer.get()
        print(f"Consumer acquired file {file_number}")

        # Print semaphore values for debugging
        print(f"Buffer full slots: {buffer_full._value}, Buffer empty slots: {buffer_empty._value}")

        mutex.release()  # Release exclusive access to the buffer
        print("Consumer released mutex (buffer slot consumed)")
        buffer_empty.release()  # Increment the empty slots in the buffer
        print("Consumer released buffer_empty semaphore (buffer slot consumed)")


        filename = f"student{file_number}.xml"
        print(f"Processing XML file: {filename}")

        # Read the XML file and process student information
        student = xml_to_student(filename)
        average = student.calculate_average()
        passed = student.passed()

        # Print student information
        print("Student Name:", student.name)
        print("Student ID:", student.student_id)
        print("Programme:", student.program)
        print("Courses and Marks:")
        for course in student.courses:
            print(f"- {course['name']}: {course['mark']}")
        print("Average:", average)
        print("Pass/Fail:", "Pass" if passed else "Fail")
        print()

        # Delete the XML file
        delete_xml_file(filename)
        print(f"Deleted file: {filename}")

    print("Consumer thread finished.")



























