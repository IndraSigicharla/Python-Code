name, age, gender, region = ([] for i in range(4))
n = int(input("Enter the number of customers: "))
for _ in range(n):
    name.extend([input("Enter the name: ")])
    age.extend([int(input("Enter the age: "))])
    gender.extend([input("Enter the gender: ")])
    region.extend([input("Enter the region: ")])
y = input("Enter the region you want to search: ")
for i, x in enumerate(region):
    if y in x:
        print(f"Name: {name[i]}", f"Age: {age[i]}", f"Gender: {gender[i]}", f"Region: {region[i]}", sep="\n")
    elif y not in region:
        print(f"The region {y} is not in our data.")
