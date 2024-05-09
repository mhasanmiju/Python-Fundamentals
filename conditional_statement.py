
# Check given number odd or even
Number = int(input("Kindly input a integer number\n"))

if Number % 2 == 0:
    print(f"{Number} is Even")
else:
    print(f"{Number} is odd")

#%%
# Update BMI.2 calculater from users weight (kg) and height(m)

Weight = float(input("Type your Weight in KG\n"))
Height = float(input("Type your Heigh in Metres\n"))
BMI = Weight/(Height)**2

if BMI < 18.5 :
    print(f" Your BMI is {round(BMI,3)},You are under weight")
elif BMI < 25:
    print(f" Your BMI is {round(BMI,3)},You are Normal weight")
elif BMI < 30:
    print(f" Your BMI is {round(BMI,3)},You are over weight")    
elif BMI < 35:
    print(f" Your BMI is {round(BMI,3)},You are Obese")
else :
    print(f" Your BMI is {round(BMI,3)},You are Clinically Obese")

#%%
#Check this year is leap year or not
#If a year divisible by 400 it's leap year if not then we need to check
# is it divisible by 4 and does not divisible by 100 then it's also a leap year
Year = int(input("Input a year\n"))

if Year % 400 == 0:
    print(f"{Year} is a Leap Year")
else :
    if Year % 4 == 0 and Year % 100 != 0:
       print(f"{Year} is a Leap Year")
    else:
        print(f"{Year} is not a Leap Year") 


#%%
   
#if height is not greater than or equal 120 cm then they can't ride
#if the age below or equal to 12 years have to pay $5 between 12 to 18 
# years have to pay $7 and for adult $12
#If any one want to take photo need to pay extra $3
print("Welcome to the Rollercoaster")
Height = float(input("Kindly input ur height in cm\n"))
Bill = 0
if Height >= 120:
        print("You can ride the Rollercoaster")
        age = int(input("Kindly input your age\n"))
        if age <12:
            Bill = 5
            print("You have to pay $5")
        elif age <= 18:
            Bill = 7
            print("You have to pay $7")
        else:
           Bill = 12
           print("You have to pay $12")
        want_photo = input("Do you want photo? type Y or N\n")
        if want_photo == "Y" or want_photo == "y" :
            Bill = Bill + 3
            print(f"After inclusion photo charge You have to pay ${Bill}")
        else :
            print(f"You don't have extra charge you have to pay ${Bill}")
else:
        print("Sorry you can\'t ride Rollercoaster")  


#%%
#Pizza delivery code
# small size $15, Medium $20 and Large $25
#Pepperoni for small $2 and medium or large $3
#Extra cheese +1
print("Welcome to Pizza World")
size = input("What size do you want: S, M or L size \n").upper()
Pepperoni= input("Do you want Pepperoni? Y or N\n").upper()
Cheese = input("Do you want Cheese? Y or N\n").upper()
Bill = 0
if size =="S" :
    if Pepperoni == "Y" :
        if Cheese =="Y":
            Bill = 15 + 2 + 1
        else :
            Bill = 15 + 2
    else:
        Bill = 15
        
elif size =="M" :
    if Pepperoni == "Y" :
        if Cheese =="Y":
            Bill = 20 + 3 + 1
        else :
            Bill = 20 + 3
    else:
        Bill = 20        
elif size =="L" :
   if Pepperoni == "Y" :
       if Cheese =="Y":
           Bill = 25 + 3 + 1
       else :
           Bill = 25 + 3
   else:
       Bill = 25
print(f"You have to Pay ${Bill}")
#%%
#Check it a Square or not
length = int(input("please input a length\n"))
width = int(input("Please input a width\n"))
if length == width :
    print("It's a Square")
else:
    print("It's not a Square")