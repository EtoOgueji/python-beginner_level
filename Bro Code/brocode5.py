#string slicing
name = "Bro Code"

#first_name = name[:3]
#last_name = name[4:]
#funky_name = name[0:8:3]
#reversed_name = name[::-1]

#print(funky_name)
#print(reversed_name)
website = "htts://google.com"


'''if website[0:5] == "https":
    slice = slice(8, -4)

elif website[0:5] == "http:":
    slice = slice(7, -4)

else:
    print("Not a valid protocol!")
    '''
slice = slice(7,-4)
print(website[slice])