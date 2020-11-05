
def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2
    
def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(string):
    return len(string)

def join_string(str_1, str_2):
    return str_1 + str_2

def add_string_as_number(str_1, str_2):
    number = int(str_1) + int(str_2)
    return number 

month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def number_to_full_month_name(number):
    month = int(number)
    if month < 1 or month > 12:
        return "Not a month"
    else:
        return month_list[month - 1 ]
# -1 as index counts from zero so subtract 1 from 1 equals 0  


def number_to_short_month_name(number):
    month = int(number)
    if month < 1 or month > 12:
        return("Not a month")
    else:
        return(month_list[month - 1 ][:3])

        # first three letters of a string 

##### FURTHER #####

def volume_of_cube(side_1):
    return(side_1**3)

# def reverse_string(string):
#     return(string.reverse)

def fahrenheit_to_celsius(temp_in_fahrenheit):
    celsius = (temp_in_fahrenheit/5) * 9
    return(celsius + 32)
