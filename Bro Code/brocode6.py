#if elif else
age = int(input("How old are you?: "))

if age >= 18:
    print("You are an adult")

elif age < 0:
    print("You haven't been born yet")

else:
    print("You are not an adult")