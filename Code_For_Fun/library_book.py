book_id, book_name, author, publisher, y_o_p, cost, no_pages, no_copies = ([] for i in range(8))
n = int(input("Enter the number of books: "))
for _ in range(n):
    b_id = int(input("Enter the Book ID: "))
    name = input("Enter the name of the book: ")
    auth = input("Enter the name of the author of the book: ")
    publ = input("Enter the name of the publisher: ")
    year = int(input("Enter the year of publication: "))
    price = int(input("Enter the price: "))
    page = int(input("Enter the number of pages: "))
    copy = int(input("Enter the number of copies available in the library: "))
    book_id.append(b_id)
    book_name.append(name)
    author.append(auth)
    publisher.append(publ)
    y_o_p.append(year)
    cost.append(price)
    no_pages.append(page)
    no_copies.append(copy)
    print()
token = 1
req_id = int(input("Enter the ID of the book you want: "))
for x in range(n):
    if book_id[x] == req_id:
        print(book_id[x], book_name[x], author[x], publisher[x], y_o_p[x],cost[x] ,no_pages[x], no_copies[x], sep='\n')
        token = 0
if token:
    print("The ID you entered does not exist within our registry.")
