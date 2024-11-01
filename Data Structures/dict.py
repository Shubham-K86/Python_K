# dictionaries are unordered collection of items.
# stored data in the form of key-value pairs.
# keys must be unique.
# it is mutable in nature means once keys created then not be changes but value changed.
# it stored any data types elements.
# symbol : {key : value}

from loguru import logger

empty_dict = {}
logger.info(type(empty_dict))

empty_dict = dict()
logger.info(type(empty_dict))

student = {"name" : "shubham","age" :27,"grade" : 24}
logger.info(student)

# accessing dictionary element
student = {"name" : "shubham","age" :27,"grade" : "A"}
logger.info(student["grade"])
logger.info(student["age"])

# accessing element using get() method. second way
logger.info(student.get("grade"))
logger.info(student.get("last_name")) # we will get none because last_name not present in dict
logger.info(student.get("last_name" ,"not available")) # here not getting none instead of getting default value.

# modifying dict elements
logger.info(student)
student["age"] = 33 # here updated the value
logger.info(student)
student["address"] = "India" # here adding new key -value element
logger.info(student)
del student["grade"] # deleting element from existing dict
logger.info(student)

# dictionary methods
keys = student.keys() # return all the keys present in dict
logger.info(keys)  
values = student.values() # return all the values present in dict
logger.info(values)
items = student.items() # return all the dict in key:value pair in form of list of tuples
logger.info(items)

# shallow copy
student_copy = student # copy existing dict to new dict student_copy
logger.info(student)
logger.info(student_copy)
student["name"] = "shubham1" # updating old dict student value
logger.info(student)
logger.info(student_copy) # here updates happen both the dict old and new
# to solve above problem we have shallow copy
student_copy1 = student.copy() # creating new dict but this time using copy() method with old dict
logger.info(student)
logger.info(student_copy1)
student["name"] = "shubham2"  # updating old dict student value
logger.info(student) # updated values visible to old dict
logger.info(student_copy1) # updated value not visible to new dict

# iterating the dictionary
# 1.can be loops to iterate over dict
# iterating using keys
for keys in student.keys() :
    logger.info(keys)
for values in student.values() :
    logger.info(values)
for keys,values in student.items() :
    logger.info(f"{keys}:{values}")

# nested dictionary
students = {
    "student1" : {"name" : "shubham","age" : 27},
    "student2" : {"name" : "divesh","age" : 29}
}
logger.info(students)

# access nested dict elements
logger.info(students["student2"]["name"])
logger.info(students["student2"]["age"])

# iterating nested dict
for student_id,student_info in students.items() :
    logger.info(f"{student_id} : {student_info}")
    for key,value in student_info.items() :
        logger.info(f"{key} : {value}")

# dictionary comprehesion
squares = {x:x**2 for x in range(5)}
logger.info(squares)

# conditional dict comprehension
evens = {x:x**2 for x in range(10) if x%2 == 0}
logger.info(evens)

# WAP to count  the frequency of element in list
numbers = [1,2,2,3,3,3,4,4,4,4]
frequency = {}
for i in numbers :
    if i in frequency :
        frequency[i] += 1
    else :
        frequency[i] = 1
logger.info(frequency)

# merge two dict into one
dict1 = {"a" : 1 ," b" : 2}
dict2 = {"b" : 3, "c" : 4}
merged_dict = {**dict1,**dict2}
logger.info(merged_dict)


