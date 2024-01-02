import random

print("Lets play the who plays the bills Game!!!")
input_names = str(input("Give me the customers names seperates by a comma \n"))
names = input_names.split(", ")
names_length = len(names) - 1
# print(names_length)
rand_int = random.randint(0, names_length)
# print(rand_int)
print(f"{names[rand_int]} pays for the bill")
