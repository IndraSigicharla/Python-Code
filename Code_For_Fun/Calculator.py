begin = input("Subject Marks Calculator. Press Enter to start or 'exit' to quit. ").lower()
if begin == "exit":
    exit("You quit the calculator.")
else:
    def main(times=3):
        for x in range(times):
            try:
                m = float(input("Enter the marks obtained in Maths: "))
                if 0 <= m <= 100:
                    pass
                else:
                    i = 2
                    while i:
                        print(f"You have {i} attempt(s) remaining.")
                        m = float(input("Enter the VALID marks obtained in Maths: "))
                        i -= 1
                        if 0 <= m <= 100:
                            break
                        elif i == 0:
                            exit("You've used up all of your remaining attempts!")
                p = float(input("Enter the marks obtained in Physics: "))
                if 0 <= p <= 100:
                    pass
                else:
                    i = 2
                    while i:
                        print(f"You have {i} attempt(s) remaining.")
                        p = float(input("Enter the VALID marks obtained in Physics: "))
                        i -= 1
                        if 0 <= p <= 100:
                            break
                        elif i == 0:
                            exit("You've used up all of your remaining attempts!")
                c = float(input("Enter the marks obtained in Chemistry: "))
                if 0 <= c <= 100:
                    pass
                else:
                    i = 2
                    while i:
                        print(f"You have {i} attempt(s) remaining.")
                        c = float(input("Enter the VALID marks obtained in Chemistry: "))
                        i -= 1
                        if 0 <= c <= 100:
                            break
                        elif i == 0:
                            exit("You've used up all of your remaining attempts!")
                sum = m + p + c
                avg = sum / 3
                if m >= 50 and p >= 50 and c >= 50:
                    print(f"You have passed in all your exams. Your total and average marks are {sum} and {avg}.")
                else:
                    print(f"You have failed in your exams. Your total and average marks are {sum} and {avg}.")
                break
            except ValueError:
                print("Please enter integer values only!!")
                pass

        end = input("Press Enter to quit or 'restart' to restart the calculator :").lower()
        if end == "restart":
            main()
        else:
            exit("You quit the calculator.")


    main()
