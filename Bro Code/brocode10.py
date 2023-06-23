# nested loops

rows = int(input("How many rows?: "))
colums = int(input("How many columns?: "))
symbol = input("Entere a symbol to use: ")

for i in range(rows):
    for j in range(colums):
        print(symbol, end = "")
    print()

