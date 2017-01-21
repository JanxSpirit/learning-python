print("Hello World!")

# variables
age=8
print(age)

one = 1
two = 2
three = one + two
print(three)

charlie_age, toby_age = 8, 6
print(charlie_age + toby_age)


x = "charlie"
y = 5
u = 9.5
print("the string is %s" % x)
print("the int is %d" % y)
print("the float is %f" % u)

#lists
my_list = []
my_list.append("i love you daddy!!!")
my_list.append(x)
my_list.append(age)
my_list.append(three)
my_list.append(toby_age)
for d in my_list:
    print(d)
print(my_list[2])

#list excercise 1
family_ages = []
family_names = []

family_names.append("daddy")
family_names.append("mommy")
family_names.append("toby")
family_names.append("charlie")

family_ages.append("6")
family_ages.append("8")
family_ages.append("42")
family_ages.append("43")

print("The names of the people in our family are:")
for name in family_names:
    print("the name is %s" % name)
print("The ages of the people in our family are:")
for age in family_ages:
    print("the age is %s"% age)
