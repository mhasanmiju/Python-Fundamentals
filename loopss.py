datas= ["Ai Engineer","Data Engineer","Data Analyst","ML Engineer"]
print(len(datas))
#strings printing in three way using loops
for i in datas:
    print(f"{i}")
print("\n")    
for i in range(3,-1,-1):
     print(f"{datas[i]}")
print("\n")
for i in range(0,4,1):
     print(f"{datas[i]}")
         
for i in range(-100, -9, 1):
    print(f"{i}")


import random

fruits = ["Apple", "Mango", "Banana", "Berry", "Orange"]
for item in fruits:
    print(item)
print(fruits)    
print(len(fruits))
    
#%%
#Calculate avarage height using loops

height = input("put some height\n").split()
print(height)

#%%
#calculate 1 to 1000 even numbers addition
sum = 0
for item in range (2, 1001, 2):
    #print(item)
    sum += item
print(f"Sum of even 1 to 10001 is = {sum}")

#calculate 1 to 1000 odd numbers addition
sum2 = 0
for item in range (1, 1001, 2):
    #print(item)
    sum2 += item
print(f"Sum of odd 1 to 10001 is = {sum2}")

#%%
#FizzBuzz game: 1 to 100 count and print but dont include if it divisible by 3 it name fizz
#divisible 5 it named buzz and divisible by both 3 and 5 it named fizzbuzz
tot = 0
for item in range(1, 101):
    if item % 3 ==0 and item % 5 ==0:
        print("FizzBuzz")
    elif item % 3 ==0:
        print("Fizz")
    elif item % 5 == 0:
        print("Buzz")
    else:
        print(item)
        tot += item
print(f"Total except FizzBuzz is = {tot}")
#%%
print("Welcome to Password generator")
password = []
num_latter = int(input("How many latter do you want in your password\n"))
num_symbol = int(input("How many symbol do you want in your password\n"))
num_number = int(input("How many number do you want in your password\n"))

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

for char in range(1, num_latter + 1):
    password.append(random.choice(letters))

for char in range(1, num_number + 1):
    password.append(random.choice(numbers))

for char in range(1, num_symbol + 1):
    password.append(random.choice(symbols))

random.shuffle(password)
print(password)

#Convert the Password List to a String
passw = ""
for char in password:
    passw += char
print(f"Your password is: {passw}")  

#%%
#user input list
lu=[]
lent= int(input("Input the length of the lis: "))
for i in range(lent):
     a = input("Input the values of the list: ")
     lu.append(a)
print(f"The list is: {lu}") 
