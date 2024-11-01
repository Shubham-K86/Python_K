# tuples are ordered collection of items.
# it is immutable in nature means it can not be change element once assigned.
# it is similar to list but tuples immutability makes it different.
# syntax : ()
 
from loguru import logger

# creating tuple
empty_tuple = ()
logger.info(type(empty_tuple))

empty_tuple = tuple()
logger.info(type(empty_tuple))

# coverting list into tuple
numbers = (1,2,3,4,5)
logger.info(type(numbers))
logger.info(numbers)

mixed_tuple = (1,"Hello World",3.14,True)
logger.info(mixed_tuple)

# accessing tuple elements
logger.info(numbers[0]) # 1
logger.info(numbers[-1]) # 5
logger.info(numbers[0:4]) # (1,2,3,4)
logger.info(numbers[::-1]) # (5,4,3,2,1)

# tuple methods
concatination_tuple = numbers + mixed_tuple # using + operator adding two tuples and make it one
logger.info(concatination_tuple)

# immutable nature of tuples
lst = [1,2,3,4,5]
logger.info(lst)
lst[1] = "shubh"
logger.info(lst) # we can chnge the value of any index in list

# logger.info(numbers)
# numbers[0] = "shubh"
# logger.info(numbers) # once value assigned in tuple then we can change it.

# tuple methods
logger.info(numbers)
logger.info(numbers.count(1)) # count() return how many times passed value prsent in tuple.
logger.info(numbers.index(3)) # index() return the indexs of passed element from tuple

# packing and unpacking tuples
# packing tuple
packed_tuple = 1,"Hello",3.14 # if we not make a tuple but it return tuple.
logger.info(packed_tuple)
# unpacking tuple
# first way
a,b,c = packed_tuple # for unpacking tuples we need to create that many variables then pass packed tuple
logger.info(a) # 1
logger.info(b) # Hello
logger.info(c) # 3.14
# second way
numbers = (1,2,3,4,5,6)
first,*middle,last = numbers
logger.info(first) # 1
logger.info(middle) # [2,3,4,5]
logger.info(last) # 6

# nested tuple
nested_tuple = ((1,2,3),("a","b","c"),(True,False))
logger.info(nested_tuple)
logger.info(nested_tuple[0]) # (1,2,3)
logger.info(nested_tuple[0][2]) # 3
# nested list
lst = [[1,2,3,4],[6,7,8,9],[1,"hello",3.14,"c"]]
logger.info(lst[0])
logger.info(lst[0][2])
logger.info(lst[0][0:3])

# iterating nested tuples
for sub_tuple in nested_tuple :
    for item in sub_tuple :
        logger.info(item,end=" ")
    logger.info()