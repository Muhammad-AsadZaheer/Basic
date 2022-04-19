#logical_Operators
#logical_operators_are_either_true/false
#operators                #denoted by
#equal to                   ==
#not equal to               !=
#less than                  <
#greater than               >
#less than or equal to      <=
#greater than or equal to   >=






print(4==4)  #4 equal  to 4
print(4!=4)  #4 is not equal to 4
print(5<4)   #5 is less than 4
print(5>4)   #5 is greater than 4
print(4<=5)  #4 is less or equal to 5
print(5>=4)  #5 is greater or equal to 4



#example for application of logical operators

# we consider a kid of some age and want to know that is his age allows him to join or school or not
#for this example minimum age required to join the school is 7

age_of_kid = (input("Please Enter the age of kid    "))                                                               #taking age from the user as input

print("here before conversion type of input is string", type(age_of_kid))                                                                                                #Here we should check the type/data type/class of input fron use

age_of_kid=int(age_of_kid)                                                                                            #by default user input is string we must have to convert is into int in this case

print("Yes it is converted into int type", type(age_of_kid))                                                                                                #after conversion of data type here we are checking it agian to verify is converted/ not

Required_age = 7                                                                                                      #as mentioned above required age is 7 so created variable for this to fix it

if(age_of_kid==Required_age):                                                                                         #comparing the age of kid and required age using if consdition
    
    print("Yes he can join school")                                                                                   #if the above given if condition is true then system will print the statement given in ""

elif(age_of_kid>Required_age):                                                                                        #here system checks if the given age of kid is more then required age

    print("Yes he is older than required age and surely he can join school")                                          #if the above elif condition is true then it will print text given in ""


else:                                                                                                                 #else condition

    (age_of_kid<Required_age)                                                                                         #here system checks less than operator only if the above given 2 operators are not satidfied/ture

    print("No His age is less than required age he should have to stay at home")                                      #it will print statement given in "" if else condition is true
