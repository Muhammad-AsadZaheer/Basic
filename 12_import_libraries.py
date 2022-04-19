#we use libraries to use the built in functions of python
#it will make coding easier

#example 1
#if we want to use the value of PI instead of initialing it manually we should use its builtin value

import math                                                                       #import math is a library
print("The value of pi is      ", math.pi)                                        #here it will show us the value of pi in output


#example two

#if want to square_root of some value we can take it using same math library

import math

x = int(input("Please Enter the vlaue           "))                                 #here we should take any number for which we want to take square roor

print("the square root of the your entered value is     ", math.sqrt(x))            #here it will return us the square root of the entered valeu


#example 3

import statistics                                                                   #we use statistics lirary to perform statistics


data = []                                                                           #created an array to store user entered values
n = int(input('Enter how many elements you want: '))                                #program will ask user how many vlaues he/she wants to enter
for i in range(0, n):                                                               #loop will start to take user entered values
    x = int(input('Enter the numbers into the array: '))                            ##user will enter valeus
    data.append(x)                                                                  #it will appened all the user entered valeus in array named as data
print(data)                                                                         #it will print entered valeus
print("Mean of your eneterd values is   ", statistics.mean(data))                   #will print the mean of entered values
print("Median of your eneterd values is ",    statistics.median(data))              #will print the median of entered values
print("Mode of your eneterd values is   ",   statistics.mode(data))                 #will print the mode of entered values