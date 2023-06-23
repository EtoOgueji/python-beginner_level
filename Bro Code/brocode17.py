# dictionary

capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Baijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'}) # Add a new K V pair
capitals.update({'USA':'Las Vegas'}) # update USA capital
capitals.pop('China') # remove key value pair
capitals.clear() # clears the dictionary


#print(capitals['Russia'])
print(capitals.get('Germany')) # to check if the key is available
print(capital.keys()) #prints only the keys
print(capitals.values()) #prints only the value

print(capitals.items()) # prints the whole dictionary

for key, value in capital.items():
    print key, values

# dictionaries are immutable

