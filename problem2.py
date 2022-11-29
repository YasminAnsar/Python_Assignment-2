##########################################################################################################
#### Question-#1
##########################################################################################################
##30.3753, 69.3451 (Pakistan)
##60.1282, 18.6435 (Sweden)
import math
## Function for calculating the distance
def distance(lat1,long1,lat2,long2):
    total_distance  = 6371.01 * math.acos(math.sin(lat1)*math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(long1 - long2))
    return total_distance
## Function to calculate the time to cover that distance 
def time(lat1,long1,lat2,long2):
    Areoplane_speed  = 740 
    time_required = distance(lat1,long1,lat2,long2)/ Areoplane_speed
    return time_required
## MAin function to take uer input and call other functions to calculate the distance and time 
def user_input():
    starting_point = input("Enter the starting country name: ")
    lat1 = math.radians(float(input("Enter the latitude1: ")))
    long1 = math.radians(float(input("Enter the longitude: ")))
    destination_point = input("Enter the destination country name: ")
    lat2 = math.radians(float(input("Enter the latitude2: ")))
    long2 = math.radians(float(input("Enter the longitude: ")))
    #result = starting_point,lat1,long1,destination_point,lat2,long2
    total_distance =  distance(lat1,long1,lat2,long2)
    time_required = time(lat1,long1,lat2,long2)
    return (f" The total distance between {starting_point} and  {destination_point} is {total_distance} and time required to complete this distance is {time_required} hours")
#Caaling the dunction 
user_input()

##########################################################################################################
#### Question-#2
###########################################################################################################
#importing statistics module for mean calculation 
import statistics              
#mean function
def mean_value(int1, int2, int3):
    numbers = (int1,int2, int3)
    mean = statistics.mean(numbers)
    return mean
#main function for user input and calling mean function
def user_values():
    int1 = int(input("Enter the first value:"))
    int2 = int(input("Enter the second value:"))
    int3 = int(input("Enter the third value:"))
    result = mean_value(int1, int2, int3)
    return (f"The mean of {int1}, {int2} and {int3} is {result}")
user_values()

##########################################################################################################
#### Question-#3
###########################################################################################################
import string  #IMPORT STRING MODULE
import re     #IMPORT FOR REGULAR EXPRESSION module
def string_input():
    mystring = str(input("Enter the text string: "))
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    new_string = regex.sub(u'', mystring)
    return new_string
string_input()
##########################################################################################################
#### Question-#4
##########################################################################################################
class_dict = {}

def class_name():
    name = input("Enter the name: ")
    score = float(input("Enter the score: "))
    class_dict[name] = (score)
    return class_dict

while(len(class_dict) < 4):
    class_name()
print(class_dict)

#########################2nd step#########################################################################
import json
import os
def class_name():
    name = input("Enter the name: ")
    score = float(input("Enter the score: "))
    class_dict[name] = (score)
    return class_dict
#an empty  file to store the dictionary data 
filename = 'class_txt_file.json'
#it will check if file already exist then it will read the data and load it into dictionary
#but here for the first time it is not already existed so it will go to else and create an empty dict and 
#second time when it will run it will store the data using if seaction
if os.path.exists(filename):
    with open(filename, 'r') as f:
        class_dict = json.load(f)
else:
    class_dict = {}
#Using while loop to take the dict values from the user and calling the class_name()
while True:    
    choice = input('You want to add more students name and score: y/n? ')  #to ask if want to add moreor not
    if choice == 'y':
        class_name()
    else:
        break
#writting into the file dict
with open(filename, 'w') as f:
    json.dump(class_dict,f)

print(class_dict)
# subtracting the score of the given name 
del class_dict['max']
print(class_dict)
##########################################################################################################
#### Question-#5
##########################################################################################################

def check_prime():
    number = int(input("Enter the number: "))
    #for loop to check the number is prime or not
    for i in range(2,number):    #i is a counter for number range.
        if number%i == 0:
            return False
    else:
        return True

check_prime()