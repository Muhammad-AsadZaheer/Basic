#we will see how if,else and elif commands work

#here we should the an exmaple for the admission of a kid into a school and  to find  that can he go to school or should he join college or he is underage.

#firsly we should take input from the user as age of student and required age for admission

age_of_boy=int(input("Please enter the age of boy "))                                                   #age of boy

required_age_for_admission=int(input("Please enter the required agefor admission in school   "))        #required_age_for_admission

if (age_of_boy  ==  required_age_for_admission):                                                        #it describes that is age of boy and required age for admission are equal if this statement is no true then it will move to elif condition

    print("yes the age of student exactly matches the required age so surely he can join school")       #if the above condition satisfies it will print the text in between "____"

elif (age_of_boy> required_age_for_admission):                                                          #the condition describes that is boy overage or not

    print("No the student is overage for school he should join college")                                #it describes that is age of boy and required age for admission are equal if this statement is no true then it will move to else condition

else:

    (age_of_boy<required_age_for_admission)                                                             #the condition describes that is boy overage or not

    print("BIG NO because the boy is underage so he should have to stay at home and enjoy his life")    #if the above condition satisfies it will print the text in between "____"
