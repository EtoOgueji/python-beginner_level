text = "Yooooooooooo\nHave a good one"

# with open("C:\\Users\\Eto Ogueji\\Desktop\\poem.txt.txt") as file:
    # print(file.read())

with open('brocode51.py', 'w') as file:
    file.write(text)


with open('brocode51.py') as file:
    print(file.read())