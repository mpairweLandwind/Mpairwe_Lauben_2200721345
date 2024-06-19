"""_summary_
    Inheritance and method overriding
    polymorphism and method resolution
    order
    Abstract classes and interfaces
    """
# Inh`eritance and method overriding`
"""_summary_
    Inheritance  and method overriding allow one object (child class)acquires all the properties and behaviors of a parent object.
    The parent object is also known as base class or super class.
    The child object is also known as derived class or sub class.
    """
#example 1: syntax: create a class where a dog inherits from the animal class and overrides the speak method.
# class Animal:
#     def speak(self):
#         return"Animal sound"

# class Dog(Animal):
#     def speak(self):
#         return"Bark"
    
#  # implementation of inherited class   
#     Animal = Animal()
#     Dog = Dog()
#     print(Animal.speak())
#     print(Dog.speak())
      
      # polymorphism allows objects of different classes to be treated the same way.
      # method resolution order allows objects of different classes to share the same method name in ahierarchy.
      
      # Example 2: how polymorphism works in python?
class Animal:
    def speak(self):
        return "mooow"
        
class Dog(Animal):
    def speak(self):
        return "Barks"
        
class Cat(Animal):
    def speak(self):
        return "Meow"

def animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()    

animal_speak(dog)
animal_speak(cat)
      
    
    
    # Exercise 1: create a simple application to manage different types of vehicles.
    #implement derived class to demonstrate inheritance and polymorphism.
"""_summary_
    1.base class: vehicle
    Attributes:make, model, year
    Methods: display_info()
    2. Derived class: 
    Car: inherits from vehicle
    attributes: number of doors
    override the display_info() method
    Motorcycle: inherits from vehicle
    attributes: type of bike(cruiser,sport,touring)
    override the display_info() method
    
    
    # Exercise 2 : create a function that accepts a list of vehicles and call the display_info() method of each vehicle in the list to display the details of each vehicle."""
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.doors}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type  # cruiser, sport, touring

    def display_info(self):
        super().display_info()
        print(f"Bike type: {self.bike_type}")

def display_vehicle_info(vehicle_list):
    for vehicle in vehicle_list:
        vehicle.display_info()

if __name__ == "__main__":
    car1 = Car("Toyota", "Camry", 2022, 4)
    motorcycle1 = Motorcycle("Honda", "CBR", 2021, "Cruiser")

    vehicle_list = [car1, motorcycle1]
    display_vehicle_info(vehicle_list)


# Reading and writing files in python
"""_summary_
    Reading and writing files in python is a very common task in programming.
    In this tutorial, we will learn how to read, open, close and write files in python.
   Keyconcepts: open(), close(), read(), write()
   description:
    open() method: opens a file and returns a file object(r,w,a,r+).
    Reading files: read() method: reads the entire contents of the file.
    Writing files: write() method: writes the contents of the file.
    close() method: closes the file.
   
    """
# example 1: write afile and read it.
with open("lauben.txt", "w") as file:
    file.write("Iam mpairwe lauben and i love python. \n")
    file.write("I use python for data science and machine learning. \n")
    
# Read from text file
with open("lauben.txt", "r") as file:
    contents = file.read()
    print(contents)    


# Handling CSV files in python
"""_summary_
    CSV stands for comma-separated values widely used for data exchange.
    CSV files are used to store tabular data.
    CSV files are plain text files.
    CSV files can be opened using any text editor.
    CSV files can be opened using any spreadsheet application.
    CSV files can be opened using any database application.
    CSV files can be opened using any programming language.
    Keyconcepts:
    Read csv files: using Csv.reader() method
    Write csv files: using Csv.writer() method
    DictReader and DictWriter. the classes are used to read and write dictionaries.
    """

# example 1 : writing and reading csv files.

import csv

# Write to csv file
with open("lauben.csv", "w",newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name","position","course"])
    writer.writerow(["mpairwe lauben","chief engineer","Software Engineering"])
    writer.writerow(["Nankunda Lilian","lecturer","computer science"])

# Read from csv file
with open("lauben.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

# example 2: using DictReader and DictWriter    
import csv

# Write to csv file
with open("lauben.csv", "w",newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["Name","position","course"])
    writer.writeheader()
    writer.writerow({"Name":"mpairwe lauben","position":"chief engineer","course":"Software Engineering"})
    writer.writerow({"Name":"Nankunda Lilian","position":"lecturer","course":"computer science"})
    
    
# JSON and XML file processing in python
"""_summary_
    JSON stands for JavaScript Object Notation.
    JSON is a lightweight data-interchange format.
    JSON is easy for humans to read and write.
    JSON is easy for machines to parse and generate.
    JSON is based on a subset of the JavaScript Programming Language, Standard ECMA-262 3rd Edition - December 1999.
    JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C-family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others.
    JSON is built on two structures:
    A collection of name/value pairs. In various languages, this is realized as an object, record, struct, dictionary, hash table, keyed list, or associative array.
    An ordered list of values. In most languages, this is realized as an array, vector, list, or sequence.
    JSON is
    
    XML stands for eXtensible Markup Language.
    XML is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable.
    
    Key concepts:
    Loading json data: using json.load() method for reading json data from a file.
    dumping json data: using json.dump() method for writing json data to a file.
    parsining json data: using json.loads() method for parsing json data from a string.
    """
# Example 6: write and read json files.
import json

# Write to json file
student_data = {
    "name": "mpairwe lauben",
    "position": "chief engineer",
    "course": "Software Engineering",
    "year": "year3"
}   

# open the file in write mode
with open("student_data.json", "w") as json_file:
    json.dump(student_data, json_file)

# Read from json file
with open("student_data.json", "r") as json_file:
    data = json.load(json_file)
    print(data)
    
# Exercise 2: Reading and writing XML files in python
# Exercise3 : Using abstraction, calculate the area and perimeter of a rectangle.
import os
import xml.etree.ElementTree as ET

# Function to create and write to an XML file
def create_xml_file(filename):
    root = ET.Element("students")

    student1 = ET.SubElement(root, "student")
    ET.SubElement(student1, "name").text = "Mpairwe Lauben"
    ET.SubElement(student1, "age").text = "21"
    ET.SubElement(student1, "major").text = "Computer Science"

    student2 = ET.SubElement(root, "student")
    ET.SubElement(student2, "name").text = "Jane Smith"
    ET.SubElement(student2, "age").text = "22"
    ET.SubElement(student2, "major").text = "Mathematics"

    tree = ET.ElementTree(root)
    with open(filename, "wb") as fh:
        tree.write(fh)

# Function to read and print content of an XML file
def read_xml_file(filename):
    if os.path.exists(filename):
        tree = ET.parse(filename)
        root = tree.getroot()

        for child in root:
            print(child.tag)
            for sub_child in child:
                print(f"  {sub_child.tag}: {sub_child.text}")
    else:
        print(f"File {filename} does not exist.")

# Create the XML file
filename = "students.xml"
create_xml_file(filename)

# Read and print the XML file
read_xml_file(filename)

        
#using abstraction to calculate the area and perimeter of a rectangle.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    