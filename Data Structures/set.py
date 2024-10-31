# set is also stored collection of unique items.
# set are unordered,means that the element do not follow any specific order.
# set not allowed duplicate items.
# set is useful when we have to remove duplicate elements,performing mathematical operation
# symbol : {}

from loguru import logger

# creation of set
my_set = {1,2,3,4,5}
logger.info(type(my_set))
logger.info(my_set)

# creating empty set
empty_set = set()
logger.info(type(empty_set))
logger.info(empty_set)

# list inside the set
coll_set = set([1,2,3,4,5])
logger.info(coll_set)

# dupliacte check 
coll_set = set([1,2,3,4,4,4,5])
logger.info(coll_set)

# set operation

# adding and removing elements
my_set = {1,2,3,4,5}
my_set.add(6)           # adding element in set
logger.info(my_set)

my_set.remove(3)  # removing element in set
logger.info(my_set)

# my_set.remove(8)  # removing element which is not present in set getting keyerror
# logger.info(my_set)

my_set.discard(8)   # it not return any error if element is not preset in set
logger.info(my_set)

# pop() method
my_set = {1,2,3,4,5}
removed_element = my_set.pop() # remove first element (FIFO) from set
logger.info(removed_element)
logger.info(my_set)

# clear() method
my_set = {1,2,3,4,5}
my_set.clear() # it will remove all the element and return empty set
logger.info(my_set)

# set membership test
my_set = {1,2,3,4,5}
logger.info(3 in my_set) # it will check the secific element present in set or not.it return true if aviable otherwise false
logger.info(10 in my_set)

# mathematical operation
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

# union
union_set = set1.union(set2) # combine both sets unique record
logger.info(union_set)

# intersection
intersection_set = set1.intersection(set2) # return matched element present in both the set
logger.info(intersection_set)

# difference
difference_set = set1.difference(set2) # return uncommon element present in set 1
logger.info(difference_set)

difference_set = set2.difference(set1) # return uncommon element present in set 2
logger.info(difference_set)

# symmetrice difference
symmetric_set = set1.symmetric_difference(set2) # return common element preset in bot the set
logger.info(symmetric_set)

# set method
set1 = {1,2,3}
set2 = {3,4,5}

# issubset()
issubset_set = set1.issubset(set2) # all the element available in set1 present in set2 if not return false
logger.info(issubset_set)

# converting list to set
lst = [1,2,2,3,4,5]
set_lst = set(lst)
logger.info(type(set_lst))
logger.info(set_lst)

# count the unquie words present on text 
text = "in this section talking about set in python"
words = text.split()
logger.info(words)
unquie_words = set(words)
logger.info(unquie_words)
logger.info(len(unquie_words))

