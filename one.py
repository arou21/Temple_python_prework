# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below.
# def hello_name(user_name):

def hello_name(user_name):
    """function to print input of username"""
    print(f"Hello {user_name}")

hello_name("Sam")

# Question 2:
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
#def first_odds():

def first_odds(num):
    """print odd numbers from 1-100"""
    while num < 101:
        print(num)
        if num == 100:
            return
        num +=2
print(first_odds(1))

# Question 3:
#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below. def max_num_in_list(a_list):


def max_num_in_list(a_list):
    """print max number in list"""
    max_val = 0
    for i in a_list:
        if max_val == None or max_val < i:
            max_val = i
    return max_val
def all_numbers():
    a_list = [1,4,19, 45]
    print("the maximum value is ", max_num_in_list(a_list))
all_numbers()


# Question 4:
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).def is_leap_year(a_year):

input_year = int(input("Enter a year:"))
def is_leap_year(a_year):
    if (a_year % 400 == 0) or (a_year % 4 == 0 and a_year % 100 !=0):
        return True
    else:
        return False

if is_leap_year(input_year):
    print(True)
else: 
    print(False)


# Question 5: 
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers,
#  but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):
# sorted

def consective_numbers(num_list):
    for i in range(0, len(num_list)-1):
        if num_list[i] +1 == num_list[i + 1] or num_list[i]-1 == num_list[i + 1]:
            return True
        else:
            return False
            break
def my_list():
    num_list = [3,5,4,2,1]
    print("The list is ", consective_numbers(num_list))
my_list()

