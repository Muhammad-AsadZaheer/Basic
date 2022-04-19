""""print("We want to print this text")                     #simplest but hectic
print("We want to print this text")
print("We want to print this text")
print("We want to print this text")
print("We want to print this text")"""


#1      #this is appraoach example of function
"""
def print_text():                                              #here we define a fuction named as print_text to print
    print("We want to print this text")
    print("We want to print this text")
    print("We want to print this text")
    print("We want to print this text")
print_text()"""

#2  #Second appraoach of function
# def print_text1():                                            # here in this approach we defined a function and defined out text which we want to print in a variable named text1, later on we just called that variable
#     text1= "We want to print this text"
#     print(text1)                                              # here we just called our variable
#     print(text1)
#     print(text1)
# print_text1()

 #3  #3rd approach

# def print_text2(text2):
#     print(text2)
#     print(text2)
#     print(text2)
# print_text2(text2="We want to print this text")

#example1 of functions

# def school_age_calculator():                                                  we defined our function named as school_age_calculator
                                                                                  
#   age_of_student=int(input("Please Enter the age of student       "))         #taking   input from user
#     
#     required_age=int(input("Please Enter the required age           "))       #taking   input from user
#     if age_of_student==required_age:                                         #it will check if condiiton     
#         print("Yes he can take admission")
#     elif age_of_student>required_age:                                         #it will check elif condiiton 
#         print("He is overage")
#     else:                                                                     #it will check else condiiton 
#         age_of_student<required_age
#         print("Sorry He cannot take admission because He is underage")
# school_age_calculator()


#example2 of functions

def future_age_prediction():
    current_age=int(input("Please Enter your current age        "))
    future_age=int(input("After how many year you want to calculate     "))
    new_age= current_age+future_age
    return new_age
future_predicted_age=future_age_prediction()
print(future_predicted_age)




