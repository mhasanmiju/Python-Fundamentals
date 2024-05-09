personName = input("What's your name?\n")
print(f'Your name is : {personName}')
Lenght_of_string = len(personName)
print(f'Length of the string is : {Lenght_of_string}')

#%%
#Type Casting
print(f'Type of the Lenght_of_string Variable: {type(Lenght_of_string)}')

# Now change it Integer to String type
newType = str(Lenght_of_string)
print(f'Newtype of Lenght_of_string Variable is: {type(newType)}')

#write a code that add two digit number e.g input 85 output 8+5=13
digit= input("Type a two digit number\n")
a = int(digit[0])
b = int(digit[1])
print(f'result is: {a+b}')

#%%
#Python Math operator follows PEMDASLR
# P = Parenthese (), E = Exponents **, M = Multiplications *
# D = Division /, A = Addition +, S = Subtraction -
# LR= left to right (Multi * and Division qulally important same as + and -)
# That is why (*/) left will get higher priority in both cases (+-)

A = (3*3+3/3-3)
print(f'According to PAMDASLR the relust is : {A}')
# answer is 7 so, Yes it follows PEMDASLR
B = (3*(3+3)/3-3)
print(f'According to PAMDASLR the relust is : {B}')
# answer is 3 so, Yes it follows PEMDASLR

#%%
#Now Write a program that calculates BMI from users weight (kg) and height(m)

Weight = float(input("Type your Weight in KG\n"))
Height = float(input("Type your Heigh in Metres\n"))
BMI = Weight/(Height)**2
print(f'Your BMI is : {BMI}')

#%%
#Create a program from your input age it will tell how many days, weeks
#and months left if your hayat to live is 90 years
year = int(input("Input your age\n"))
l_year = 90 - year
#count is include leap year
days = (l_year/4)+(l_year*365)
weeks = l_year * 52.1786
months = l_year * 12
print(f"{l_year} Years = {days} Days, {int(weeks)} Weeks and {months} Months")

#%%
print("Welcome to tip calculator")
Total_bill = float(input("Put your total bill please\n"))
Tip_percentage = int(input("Kindly type your tip Percentage from these options 10 or 12 or 15\n"))
Bill_include_tip = Total_bill + (Total_bill * (Tip_percentage/100))
print(f"Total bill after tip include{Bill_include_tip}")
#How many people slit the bill
Total_person= float(input("How many people split the bill\n"))
Each_person_bill = Bill_include_tip / Total_person
print(f"Each person need to pay {round(Each_person_bill,2)}")