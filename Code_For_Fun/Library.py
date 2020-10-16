l=[]
class Library:
    def __init__(self,books_dict):
        self.books_dict=books_dict
    def display(self):
        print("The books that are available for Students are:")
        print("\n".join(self.books_dict.values()))

    def __str__(self):
        string="\n".join([str(x) for x in self.books_dict.keys()]) #OR "\n".join(map(str,self.books_dict.keys()))
        return string

class Student(Library):
    def __init__(self,books_dict):
        super().__init__(books_dict)
    def bookChoose(self):
        global l
        print("Choose your book by selecting the following keys:")
        for x in self.books_dict.keys():
            print(f"Key {x} is for {self.books_dict[x]}")
        while(True):
            try:    
                a=int(input("Select the key:\n"))
                print("The book that you issued is {}".format(self.books_dict[a]))
                l.append(self.books_dict[a])
                del self.books_dict[a]
                break
            except ValueError:
                print("Invalid! Try again!")
    def issueOrNot(self):
        global l
        index=1
        while(True):
            # print("The books available for issue are\n"+ "\n".join(self.books_dict.values()))
            # response=input("Do you wanna issue another book?Y/N\n")
            if(index<3):
                print("The books available for issue are\n"+ "\n".join(self.books_dict.values()))
                response=input("Do you wanna issue another book?Y/N\n").upper()
                if response=='Y':
                    while(True):
                        try:
                            a=int(input("Select the key:\n"))
                            print("The book that you issued is {}".format(self.books_dict[a]))
                            l.append(self.books_dict[a])
                            del self.books_dict[a]
                            index+=1
                            break
                        except ValueError:
                            print("Invalid literal for key! Try again!")
                        except KeyError:
                            print("Invalid Key! Make sure you are entering a key that exists!")
                elif response=='N'.upper():
                    exit("Thanks for issuing the book(s) from this Library.Don't forget to return the book(s),"+ ",".join(l)+ " after a week! Thank You!")
                else:
                    print("Invalid! Try again!")
            else:
                exit("You cannot issue any more books! Thank you! Enjoy and don't forget to return the book(s)," + ",".join(l) + " back after a week.")

if __name__=="__main__":
    # books=Library({1:"Let Us C",2:"Let us C++",3:"Automate the boring stuff with Python",4:"Kali Linux Revealed",5:"Python programming"})
    books=Student({1:"Let Us C",2:"Let us C++",3:"Automate the boring stuff with Python",4:"Kali Linux Revealed",5:"Python programming"})
    books.display()
    # print(books)
    books.bookChoose()
    books.issueOrNot()