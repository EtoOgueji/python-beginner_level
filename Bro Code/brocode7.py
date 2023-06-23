# logical operators

temp = int(input("What is the temperature outside?: "))

# some real AI(Brixton) shit
''' if temp >= 0 and temp <= 30:
    print("The temperature is good today: ")
    print("Go Outside: ")

elif temp < 0 or temp > 30:
    print("The temperature is bad today!")
    print("Stay inside")
'''

if not(temp >= 0 and temp <= 30):
    print("The temperature is good today: ")
    print("Go Outside: ")

elif not(temp < 0 or temp > 30):
    print("The temperature is bad today!")
    print("Stay inside")