def main():
    try:
        score = float(input("Enter your CGPA :"))
        if score > 10 or score < 0:
            print("Invalid score.")
            main()
        elif 9 <= score <= 10:
            print("Outstanding!!")
        elif 8 <= score < 9:
            print("Excellent!")
        elif 7 <= score < 8:
            print("Good.")
        elif 6 <= score < 7:
            print("Average.")
        elif 5 <= score < 6:
            print("Better.")
        else:
            print("Poor.")
    except ValueError:
        print("Please enter VALID score!")
        main()
main()
