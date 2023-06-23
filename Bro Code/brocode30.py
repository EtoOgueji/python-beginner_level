# str.format() = optional method that gives users more control when displaying output

# animal = "cow"
# item = "moon"

# print("The {} jumped over the {}".format(animal, item))
# print("The {} jumped over the {}".format('cow', 'moon'))

# postional argument
# print("The {1} jumped over the {0}".format(animal, item))
# print("The {1} jumped over the {1}".format(animal, item))
#printf("The {item} jumped over the {animal}".format(animal = "cow", item = "moon"))

text = "The {} jumped over the {}"
print(text.format(animal, item))