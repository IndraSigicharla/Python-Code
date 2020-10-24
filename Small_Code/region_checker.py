name, age, gender, region = ([] for i in range(4))
n = int(input("Enter the number of customers: "))
for x in range(n):
    name.append(input("Enter the name: "))
    age.append(int(input("Enter the age: ")))
    gender.append(input("Enter the gender: "))
    region.append(input("Enter the region: "))
y = input("Enter the region you want to search: ")
for i in range(n):
    if y == region[i]:
        print(f"Name: {name[i]}", f"Age: {age[i]}", f"Gender: {gender[i]}", f"Region: {region[i]}", sep="\n")
    else:
        print(f"The region {y} is not in our data.")