from loguru import logger
# list in python is consider as an data structure.
# list contain any type of data tyeps elements/stored any data type elements inside the list. 
# list is mutable in nature so we can add/delete/update the list.
# list are ordered in nature.

# lst = []
# logger.info(type(lst))

# names = ["krish","jack","jacob",1,2,3,4,5]
# logger.info(names)

# mixed_list = ["krish","jack",True,35.78,9]
# logger.info(mixed_list)

# accessing the list
fruits = ["apple","banaba","cherry","kiwi","gauva"]
# logger.info(fruits[0])
# logger.info(fruits[0:3])
# logger.info(fruits[:1])
# logger.info(fruits[-1])
# logger.info(fruits[::-1])

# modifying the list element
# logger.info(fruits)
# fruits[1] ="watermelon"
# logger.info(fruits)

# list methods
# fruits.append("orange")  # add an item to the end of the list
# logger.info(fruits)

# fruits.insert(1,"mango") # insert the item in specific index
# logger.info(fruits)

# fruits.remove("kiwi") # remove the item from the list
# logger.info(fruits)

# poped_fruits = fruits.pop() # remove the last element from the list and return remove element in terminal. pop() want to store o/p in one variable
# logger.info(poped_fruits)
# logger.info(fruits)

# index = fruits.index("mango") # return the index number of give item frm list
# logger.info(index)

# fruits.insert(3,"cherry")
# logger.info(fruits.count("cherry"))

# fruits.sort() # sort the list in asc order
# logger.info(fruits)

# fruits.reverse() # this will reverse the list
# logger.info(fruits)

# fruits.clear() # clear() used to clear the list
# logger.info(fruits)

# slicing list
numbers = [1,2,3,4,5,6,7,8,9]
# logger.info(numbers)
# logger.info(numbers[2:5])  # 3,4,5
# logger.info(numbers[:5]) # 1,2,3,4,5
# logger.info(numbers[5:]) # 6,7,8,9
# logger.info(numbers[::2]) # 1,3,5,7,9 here 2 is the jump num
# logger.info(numbers[::-1]) # 9,8,7,6,5,4,3,2,1

# iterating over list
# for index,number in enumerate(numbers) :
#     logger.info(f"index : {index} value : {number}")

# for number in range(len(numbers)) :
#     logger.info(f"index : {number} value : {numbers[number]}")

# list comprehension
# syntax :
# [expression for item in iterable]
# synatax with conditional logic
# [expression for item in iterable if condition]

# WAP for square of number
lst = []
for x in range(10) :
    lst.append(x**2)
logger.info(lst)

lst = [x**2 for x in range(10)]
logger.info(lst)

# WAP for even  number
even_number = [i for i in range(10) if i % 2 == 0]
logger.info(even_number)

# nested list comprehension
# syntax
# [expression for item1 in iterable for item2 in iterable]

lst1 = [1,2,3,4]
lst2 = ['a','b','c','d']
paired_lst = [(i,j) for i in lst1 for j in lst2]
logger.info(paired_lst)

# list comprehension with function call
fruits = ["apple","banaba","cherry","kiwi","gauva"]
len_count = [len(count) for count in fruits]
logger.info(len_count)