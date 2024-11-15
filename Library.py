import pymysql

mydb = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database="library")

mycursor = mydb.cursor()

lst = []


def add_books():
    while True:
        while True:
            bookname = input("\nPlease enter book's name: ")
            if bookname.isspace() or bookname.isdigit() or not bookname.isalnum():
                print("Invalid input, please only use a-z characters...")
                continue
            else:
                lst.append(bookname)
                if bookname == "end" or bookname == "quit" or bookname == "exit":
                    exit()
                break
        while True:
            authorname = input("\nPlease enter author's name: ")
            if authorname.isspace() or not authorname.isalpha():
                print("Invalid input, please only use a-z characters...")
                continue
            else:
                lst.append(authorname)
                if authorname == "end" or authorname == "quit" or authorname == "exit":
                    exit()
                break
        while True:
            yearofpublication = input("\nPlease enter years of book publication: ")
            if yearofpublication.isspace() or not yearofpublication.isdecimal() or yearofpublication[0] == "0" or len(yearofpublication) != 4:
                print("Invalid input, please only use numbers or enter a valid input...")
                continue
            else:
                lst.append(yearofpublication)
                if yearofpublication == "0":
                    exit()
                break

        sql_command = """
        INSERT INTO books_info(Book_name,Author_name,Year_of_publication)
        VALUES (%s,%s,%s)
        """

        mycursor.execute(sql_command, list(lst))
        mydb.commit()
        print(mycursor.rowcount, "Book added to database successfully...")
        while True:
            b_or_c = input("\nTo continue adding press y or no press n: ")
            if b_or_c == "y":
                print("Continue, please wait...")
                break
            elif b_or_c == "n":
                print("Thanks for follow this program...\n\rExit...")
                exit()
            else:
                print("Invalid input, please only enter y or n...")
            continue


def show_books():
    sql_command = """
    SELECT * FROM books_info
    """
    mycursor.execute(sql_command)
    result = mycursor.fetchall()
    mydb.commit()
    for i in result:
        print(i)


def edit_books():
    lst2 = []
    while True:
        sql_command = """
        SELECT * FROM books_info
        """
        mycursor.execute(sql_command)
        result = mycursor.fetchall()
        for i in result:
            print("\n", i, end="")

        msg = input("\n\nPlease enter the name of book to edit: ")
        while True:
            bookname = input("\nPlease enter book's name: ")
            if bookname.isspace() or bookname.isdigit() or not bookname.isalnum():
                print("Invalid input, please only use a-z characters...")
                continue
            else:
                lst2.append(bookname)
                if bookname == "end" or bookname == "quit" or bookname == "exit":
                    exit()
                break
        while True:
            authorname = input("\nPlease enter author's name: ")
            if authorname.isspace() or not authorname.isalpha():
                print("Invalid input, please only use a-z characters...")
                continue
            else:
                lst2.append(authorname)
                if authorname == "end" or authorname == "quit" or authorname == "exit":
                    exit()
                break
        while True:
            yearofpublication = input("\nPlease enter years of book publication: ")
            if yearofpublication.isspace() or not yearofpublication.isdecimal() or yearofpublication[0] == "0" or len(yearofpublication) != 4:
                print("Invalid input, please only use numbers or enter a valid input...")
                continue
            else:
                lst2.append(yearofpublication)
                if yearofpublication == "0":
                    exit()
                break
        lst2.append(msg)
        sql_command1 = """
        UPDATE books_info SET Book_name = %s,Author_name = %s,Year_of_publication = %s WHERE Book_name = %s
        """

        mycursor.execute(sql_command1, list(lst2))
        mydb.commit()
        print(mycursor.rowcount, "book edited in database successfully...")
        while True:
            b_or_c = input("\nTo continue editing press y or no press n: ")
            if b_or_c == "y":
                print("Continue, please wait...\n")
                break
            elif b_or_c == "n":
                print("Thanks for follow this program...\n\rExit...")
                exit()
            else:
                print("Invalid input, please only enter y or n...")
            continue


def delete_books():
    while True:
        sql_command = """
        SELECT * FROM books_info
        """
        mycursor.execute(sql_command)
        result = mycursor.fetchall()
        for i in result:
            print("\n", i, end="")

        msg = input("\n\nPlease enter the name of book to delete: ")
        sql_command1 = """
        DELETE FROM books_info WHERE Book_name = %s
        """

        mycursor.execute(sql_command1, msg)
        mydb.commit()
        print(mycursor.rowcount, "book deleted from database successfully...")
        while True:
            b_or_c = input("\nTo continue deleting press y or no press n: ")
            if b_or_c == "y":
                print("Continue, please wait...\n")
                break
            elif b_or_c == "n":
                print("Thanks for follow this program...\n\rExit...")
                exit()
            else:
                print("Invalid input, please only enter y or n...")
            continue


msg = input("Please select a command word to continue\n(Add_A, Show_S, Edit_E, Delete_D): ")
if msg == "Add" or msg == "A":
    print("Add books...")
    add_books()
elif msg == "Show" or msg == "S":
    print("Show books...")
    show_books()
elif msg == "Edit" or msg == "E":
    print("Edit books...")
    edit_books()
elif msg == "Delete" or msg == "D":
    print("Delete books...")
    delete_books()
else:
    print("Invalid input\nExit...")
    exit()
