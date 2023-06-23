# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)

# dinner_table = utensils.union(dishes)

# print(utensils.difference(dishes))  # comparing the two sets to check what they don't have in common

print(utensils.intersection(dishes))



for x in dinner_table:
    print(x)

