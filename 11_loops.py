#we have two loops while and for loops
#repition of same work is called loop, untill the imposed condition is satisfies
#first we would look while loops

#while loop
x=0                                                                    #intialized x with 0
while(x<13):                                                          #it will run untill the value of x is less then 13
    print(x)                                                          #if value of x is less then 13 then print the vlaue of x
    x=x+1                                                             #everytime after prinitng the value of adds one in 1


#for loop


for x in range(0,9):                                                  #value of x starts from 0 and less than 9
    print(x, "we printing the value of x")                            #if the above condition satisfies then print value of x and text along the value of x


a=0                                                                   #took variables a,b
b=9
for x in range(a,b):
    print(x, "we printing the value of x")



#example1

days= ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]                 #create an array with valeus from mon to sun
for d in days:                                                          #uses a for loop    
    if ( d=="Sat"): break                                               #if when the value of days is equal to day sat it will break means that it will stop
   # if (d=="Sat"): continue                                            #if when the value of days is equal to day sat it will skip sat and moves on sun
    print(d)                                                            #here it will print the value of days