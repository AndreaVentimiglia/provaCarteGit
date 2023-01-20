# importing sys
from module1 import odd_even, add
import sys

# adding Folder_2 to the system path
sys.path.append('../')

# importing the add and odd_even
# function

# calling odd_even function
odd_even(5)

# calling add function
print("Addition of two number is :", add(2, 2))
