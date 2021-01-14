import os
import re
details = []
ml = ['Movie 1', 'Movie 2', 'Movie 3', 'Movie 4', 'Movie 5']
tl = ['Theater 1', 'Theater 2', 'Theater 3', 'Theater 4', 'Theater 5']
sl = ['12:30 PM - 2:30 PM','3:00 PM - 5:00 PM','5:30 PM - 7:30 PM','8:00 PM - 10:00 PM','10:30 PM - 12:30 AM']
mml, mtl, msl, tc = ([] for _ in range(4))  # Used lists and generators
i = 0


class Theater:  # Used classes
    def __init__(self, movie_list):
        self.movie_list = movie_list

    def display(self):  # Used functions
        print("\nThe movies that are available near you are: ")
        for i, j in enumerate(self.movie_list, 1):  # Used lists and for loops
            print(f"{i}) {j}")

    def cancellation(self):  # Used functions
        m = input("\nDo you want to cancel the booked tickets? (Yes / No) ").lower()
        if m == "yes":
            if len(mml) == 0:
                print("\nYou don't have any shows booked.")
            else:
                print("\nYou have these shows booked.")
                for i, j in enumerate(zip(mml, mtl, msl, tc), 1):
                    print(f"{i})", *j)
                x = int(input("\nWhich show do you want to cancel? "))
                if x in range(len(mml)+1):
                    mml.pop(x-1)
                    mtl.pop(x-1)
                    msl.pop(x-1)
                    tc.pop(x-1)
                else:
                    print("Not a valid input.")
                    movie.cancellation()

        elif m != "no":
            print("\nNot a valid response, please try again.")
            movie.cancellation()
        movie.quitter()

    def booking(self):  # Used functions
        if len(mml) == 0:
            print("You don't have any shows booked right now.")
        else:
            print("These are the shows that you have upcoming.")
            for i, j in enumerate(zip(mml, mtl, msl, tc), 1):
                print(f"{i})", *j)
        movie.quitter()

    def search(self):  # Used functions
        x = input("Enter the title of the movie you are searching for: ")
        if x in ml:
            y = input("This movie is available to be booked on our app. Would you like to be redirected there? (Yes / No) ").lower()
            if y == "yes":
                movie.display()
                movie.movieChoose()
            elif y == "no":
                movie.quitter()
            else:
                print("Invalid Input.")
                movie.search()
        else:
            print("Sadly, we do not have this movie in our catalogue.")
            movie.quitter()

    def quitter(self):
        m = int(input("Enter 1 to go back to the menu, or 0 to quit the application: "))
        if not m:
            print("Goodbye!!")
            os._exit(0)
        else:
            MoviePerson.menu()

    def __str__(self):
        return "\n".join(self.movie_list)


class MoviePerson(Theater):
    def __init__(self, movie_list):
        super().__init__(movie_list)

    def registration(self):
        global details
        os.system("cls")
        print("Welcome, new user! Please create a new account to login.\n")
        name = input("Please enter your name: ")
        details.append(name)
        while True:
            try:
                age = int(input("Please enter your age: "))
                if 18 <= age < 120:
                    details.append(age)
                    break
                else:
                    print("Invalid age. Please enter again.")
            except ValueError:
                print("Invalid! Try again!")

        checker = r"^\w+[\._]?[a-z0-9]+@{1}\w+[.]\w+$"  # Used regex

        while True:
            email = input("Enter your Email ID: ")
            if re.search(checker, email):
                details.append(email)
                break
            else:
                print("Invalid Email. Please enter again.")

    def menu():  # Used functions
        global i
        if i == 0:
            print("\n===============================================")
            print(f"Welcome {details[0]}, what would you like to do?")
            print("===============================================")
        i+=1
        m = int(input("1) Book movie tickets\n2) Cancel tickets\n3) Check all bookings\n4) Search for movies\n5) Quit\n"))
        if m == 1:
            movie.display()
            movie.movieChoose()
        elif m == 2:
            movie.cancellation()
        elif m == 3:
            movie.booking()
        elif m == 4:
            movie.search()
        elif m == 5:
            print("Goodbye!!")
            os._exit(0)
        else:
            print("Invalid option, choose again.")
            MoviePerson.menu()

    def movieChoose(self):
        global mml
        while 1:
            try:
                a = int(input("Select the movie of your liking: "))
                if a not in range(len(ml)+1):
                    print("\nThis is not a valid choice, please select the movie again.")
                    movie.display()
                    movie.movieChoose()
                elif self.movie_list[a-1] in mml:
                    print(f"\nThe movie that you chose is {self.movie_list[a-1]}.")
                    print("\nYou've already booked a ticket for this movie!")
                    movie.display()
                    movie.movieChoose()
                else:
                    print(f"\nThe movie that you chose is {self.movie_list[a-1]}.")
                    mml.append(self.movie_list[a-1])
                    movie.theaterSelector()
                break
            except ValueError:
                print("Invalid! Try again!")

    def theaterSelector(self):
        print("The movie you have picked is available at these theaters. Please select one:\n")
        for i, j in enumerate(tl, 1):
            print(f"{i}) {j}")
        x = int(input())
        if x in range(len(tl)+1):
            mtl.append(tl[x-1])
            movie.timingSelector()
        else:
            print("That is not a valid theater, please enter again.")
            movie.theaterSelector()

    def timingSelector(self):
        print("The theater you chose has these timings available for your movie. Please select a suitable one:\n")
        for i, j in enumerate(sl, 1): # Used lists
            print(f"{i}) {j}")
        x = int(input())
        if x in range(len(sl) + 1):
            msl.append(sl[x - 1])
            movie.ticketCount()
        else:
            print("That is not a valid theater, please enter again.")
            movie.timingSelector()

    def ticketCount(self):
        x = int(input("How many tickets do you need? Please enter under the max amount of 30:\n"))
        if x not in range(31):
            print("Not a valid count, please enter again.")
            movie.ticketCount()
        else:
            tc.append(f"{x} ticket(s)")  # Used lists
            movie.quitter()


movie = MoviePerson(ml)  # Driver code, initiates the object "movie" with the list of movies
movie.registration()  # Takes care of the registration of the user
MoviePerson.menu()  # Shows the menu to get the user started
