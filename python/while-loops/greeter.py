prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello,  " + name + "!")

age = input("How old are you? ")
age = int(age)
print(age >= 18)

height = input("\nHow tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
