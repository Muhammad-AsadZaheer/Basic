#there are two approacehs for type conversion 1) implicit 2) explicit
#let suppose we have 3 variables with 3 diferent types

#first lets see implicit appraoch

x=10               #integer
y=10.11            #float
z= "abc"           #string


#lets check variables types

print(x,"type of x is variable is ", (type(x)))                                              #in next three lines it will check the value and type of each variable
print(y,"type of y is variable is ", (type(y)))
print(z,"type of z variable is ", (type(z)))

#lets  try addition on x and y variables and it will change x type

x=x+y                                                                                        #it will change the type and value of x and this appraoch is called implicit

print(x, "Now the type of x is ", (type(x)))


#Now lets move on explicit approach

#it also have two ways firstly we are looking for apprach 1
#lets take input from user and user input is by default string and will it change it to int



user_input= input("Hello user please enter your input     ")                                 #taking input from user

print(user_input,  "Here The type of the user input is " , type(user_input))                 #it will show us the type of user input

user_input=int(user_input)                                                                   #converting the type of user_input

print(user_input,  "The type of the user input is " , type(user_input))


#method 2 for explicit approach


user_input= input("User please enter your age   ")                                           #taking user age as input

print(user_input,  "Here The type of the user age is " , type(user_input))                   #it will show us the type of user input

print(user_input,  "The type of the user age is " , (type(int(user_input))))                 #here it will change the type of user age and show us