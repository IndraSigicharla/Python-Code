begin = input("Subject Marks Calculator. Press Enter to start or 'exit' to quit. ").lower()
if begin == "exit":
    exit("You quit the calculator.")
else:
    def main(times=3):
        for _ in range(times):
            try:
                m = float(input("Enter the marks obtained in Maths: "))
                if m not in range(101):
                    i = 2
                    while i:
                        print(f"You have {i} attempt(s) remaining.")
                        m = float(input("Enter the VALID marks obtained in Maths: "))
                        i -= 1
                        if m in range(101):
                            break
                        elif i == 0:
                            exit("You've used up all of your remaining attempts!")
                p = float(input("Enter the marks obtained in Physics: "))
                if p not in range(101):
                    i = 2
                    while i:
                        print(f"You have {i} attempt(s) remaining.")
                        p = float(input("Enter the VALID marks obtained in Physics: "))
                        i -= 1
                        if p in range(101):
                            break
                        elif i == 0:
                            exit("You've used up all of your remaining attempts!")
                c = float(input("Enter the marks obtained in Chemistry: "))
                if c not in range(101):
                    i = 2
                    while i:
                        print(f"You have {i} attempt(s) remaining.")
                        c = float(input("Enter the VALID marks obtained in Chemistry: "))
                        i -= 1
                        if c in range(101):
                            break
                        elif i == 0:
                            exit("You've used up all of your remaining attempts!")
                sum = m + p + c
                avg = sum / 3
                if m and p and c not in range(50):
                    print(f"You have passed in all your exams. Your total and average marks are {sum} and {avg:.3f}.")
                else:
                    print(f"You have failed in your exams. Your total and average marks are {sum} and {avg:.3f}.")
                break
            except ValueError:
                print("Please enter integer values only!!")
        end = input("Press Enter to quit or 'restart' to restart the calculator :").lower()
        if end == "restart":
            main()
        else:
            exit("You quit the calculator.")


    main()
