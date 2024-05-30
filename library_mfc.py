books = []

def add_book():
    book_id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = int(input("Enter publication year: "))
    genre = input("Enter genre: ")
    loc = input("Enter location (format: fxrycz) where x,y and z are floor,row and column: ")
    copies = int(input("Enter number of copies: "))
    books.append({"id": book_id, "title": title, "author": author, "year": year, "genre": genre, "location": loc, "copies": copies})
    print("Book added successfully.")

def get_book():
    print("NOTE: To know book ID of book needed view the nooks through display menu")
    book_id = int(input("Enter book ID to retrieve: "))
    for book in books:
        if book["id"] == book_id:
            if book["copies"] > 0:
                book["copies"] -= 1
                print("Book retrieved successfully.")
            else:
                print("No copies available for this book.")
            return
    print("Book not found.")

def update_book():
    book_id = int(input("Enter book ID to update quantity: "))
    for book in books:
        if book["id"] == book_id:
            quantity = int(input("Enter new quantity: "))
            book["copies"] = quantity
            print("Quantity updated successfully.")
            return
    print("Book not found.")

def delete_book():
    book_id = int(input("Enter book ID to delete: "))
    for i, book in enumerate(books):
        if book["id"] == book_id:
            del books[i]
            print("Book deleted successfully.")
            return
    print("Book not found.")

def display_books():
    print("Display Options:")
    print("1. Display all books")
    print("2. Display books by genre")
    print("3. Display books by author")
    choice = input("Enter your choice: ")

    if choice == "1":
        for book in books:
            print_book_details(book)
    elif choice == "2":
        display_books_by_genre()
    elif choice == "3":
        display_books_by_author()
    else:
        print("Invalid choice.")

def display_books_by_genre():
    genre = input("Enter genre to display books: ")
    genre_books = [book for book in books if book["genre"].lower() == genre.lower()]
    if genre_books:
        for book in genre_books:
            print_book_details(book)
    else:
        print(f"No books found in the genre '{genre}'.")

def display_books_by_author():
    author = input("Enter author to display books: ")
    author_books = [book for book in books if book["author"].lower() == author.lower()]
    if author_books:
        for book in author_books:
            print_book_details(book)
    else:
        print(f"No books found by the author '{author}'.")

def print_book_details(book):
    print(f"ID: {book['id']}\nTitle: {book['title']}\nAuthor: {book['author']}\nYear: {book['year']}\nGenre: {book['genre']}\nLocation: {book['location']}\nCopies: {book['copies']}")

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Get Book")
    print("3. Update Book Quantity")
    print("4. Delete Book")
    print("5. Display Books")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        get_book()
    elif choice == "3":
        update_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        display_books()
    elif choice == "6":
        print("~Exiting")
        break
    else:
        print("Invalid choice. Please try again.")
