# Day one printing and find the data types
print("\"Hello World!\"")
print("Miju" + " " + '(Data Scientist)\n')
print("Hello" + " " + input("What\'s Your name?") + "!\n")

#%%
a = input("Type 1st Number\n")
b = input("Type 2nd Number\n")
print(f'Output of a: {a}')
print(f'Output of b: {b}')
c = a
a = b
b = c
print(f'Output after swap of a to b: {a}')
print(f'Output after swap of b to a of b: {b}')

#%%
print("Welcome to Band Name Generetor")
personCity = input("Which City Did you grow up in:\n")
petName = input("What\'s your pet name\n")
print(f'Your Band name is: {personCity}{petName}')