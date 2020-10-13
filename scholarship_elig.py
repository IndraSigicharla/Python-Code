begin = input("Are you a first graduate? (Yes/No)").lower()
if begin == "yes":
    pass
else:
    exit("This scholarship is only for first graduates.")
def main():
    try:
        m1 = float(input("Enter the Maths marks: "))
        m2 = float(input("Enter the Physics marks: "))
        m3 = float(input("Enter the Chemistry marks: "))
        avg = (m1 + m2 + m3) / 3
        if avg > 98:
            print("You are eligible for the scholarship!")
        else:
            exit("You haven't qualified for the scholarship.")
    except ValueError:
        print("Enter valid marks!!")
        main()
main()