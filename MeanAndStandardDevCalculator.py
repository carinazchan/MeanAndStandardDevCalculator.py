'''
FUNCTION DEFINITIONS & MODULES
'''

#Math module.
import math

#Function: Sorted list.
def print_sorted(num_list):
    num_list.sort()
    print("This is your sorted list of numbers:")
    print(num_list)

#Function: Computing mean.
def compute_mean(num_list):
    num_list_mean = sum(num_list) / len(num_list)
    return num_list_mean

#Function: Computing variance.
def compute_variance(num_list):
    numerator_final = 0 #Initialize numerator_final.
    for x in num_list: #For-loop to calculate the numerator.
        numerator_part1 = x - compute_mean(num_list)
        numerator_part2 = math.pow(numerator_part1, 2)
        numerator_final += numerator_part2
    num_list_variance = numerator_final / len(num_list) #Calculates the variance.
    return num_list_variance

#Function: Computing standard deviation.
def compute_standard_dev(num_list_variance):
    return math.sqrt(num_list_variance) #Calculates the square root of variance.


'''
MAIN PROGRAM
'''

#Asks user for input, converts to integer.
current_num = int(input("Please input a positive integer: "))
print()
num_list = [] #Initialize num_list as empty list.

#Checks if current_num is an integer, returns True or False.
if_int = isinstance(current_num, int)

#While-loop to reprompt user for another integer.
while if_int == True:
    if current_num >= 0: #If current_num positive.
        num_list.append(current_num) #Adds on current_num to num_list.
        current_num = int(input("Please input another integer: ")) #Asks for another
        print()                                                    #integer.
    else: #If current_num negative.
        if_int = False #Stops while-loop.

print_sorted(num_list)
print("The mean is:", compute_mean(num_list))
print("The standard deviation is:",\
compute_standard_dev(compute_variance(num_list)))
