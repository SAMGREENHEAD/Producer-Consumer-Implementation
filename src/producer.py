import multiprocessing as mp
import random
import xml.etree.ElementTree as ET
from buffer import buffer, buffer_full, buffer_empty, mutex
from student import ITstudent
import time

END_OF_FILES = -1


# Generate random student information
def generate_random_student():
    name = "Student " + str(random.randint(1, 100))
    student_id = str(random.randint(10000000, 99999999))
    program = random.choice(['Computer Science', 'Information Technology'])
    num_courses = random.randint(1, 5)
    courses = []
    for _ in range(num_courses):
        course_name = "Course " + str(random.randint(1, 10))
        mark = random.randint(0, 100)
        courses.append({'name': course_name, 'mark': mark})
    return ITstudent(name, student_id, program, courses)

# Convert student object to XML string
def student_to_xml(student):
    root = ET.Element('student')
    name_element = ET.SubElement(root, 'name')
    name_element.text = student.name
    id_element = ET.SubElement(root, 'id')
    id_element.text = student.student_id
    program_element = ET.SubElement(root, 'program')
    program_element.text = student.program
    courses_element = ET.SubElement(root, 'courses')
    for course in student.courses:
        course_element = ET.SubElement(courses_element, 'course')
        name_element = ET.SubElement(course_element, 'name')
        name_element.text = course['name']
        mark_element = ET.SubElement(course_element, 'mark')
        mark_element.text = str(course['mark'])
    return ET.tostring(root, encoding='unicode')

def producer(producer_id,event):
    for i in range(1, 11):
        student = generate_random_student()
        xml_data = student_to_xml(student)
        filename = f"student{producer_id}_{i}.xml"

        buffer_empty.acquire()  # Wait for an empty slot in the buffer
        mutex.acquire()  # Acquire exclusive access to the buffer

        # Add the file number to the buffer
        buffer.put(i)
        print(f"Producer {producer_id} produced file {i}")

        # Write the XML data to the file
        with open(filename, 'w') as file:
            file.write(xml_data)
        print(f"Producer {producer_id} wrote XML data to {filename}")

        mutex.release()  # Release exclusive access to the buffer
        buffer_full.release()  # Increment the full slots in the buffer
        print(f"Producer {producer_id} released buffer_full semaphore")


    time.sleep(2)    
    buffer.put(END_OF_FILES)
    print(f"Producer {producer_id} finished producing.")
    # Set the event to signal the consumer to finish
    event.set()

# Create and start the producer processes
if __name__ == '__main__':
    num_producers = 2  # Adjust the number of producers as needed

    producer_processes = []
    for i in range(num_producers):
        producer_process = mp.Process(target=producer, args=(i,))
        producer_processes.append(producer_process)
        producer_process.start()

    # Wait for all producer processes to finish
    for producer_process in producer_processes:
        producer_process.join()
