import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Students"
)
mycursor = mydb.cursor()


def add_students():
    students_info = {}
    while True:
        while True:
            First_name = input("Please enter 1st student's first name: ").strip()
            if First_name.isdigit():
                print("Invalid input, Please only use (a-z & A-Z) characters\n")
                continue
            if First_name == "":
                print("Invalid input, The entered value must not be empty\n")
                continue
            else:
                students_info["firstname"] = First_name
            break
        while True:
            Last_name = input("Please enter 1st student's last name: ").strip()
            if Last_name.isdigit():
                print("Invalid input, Please only use (a-z & A-Z) characters\n")
                continue
            elif Last_name == "":
                print("Invalid input, The entered value must not be empty\n")
                continue
            else:
                students_info["lastname"] = Last_name
            break
        while True:
            UID = input("Please enter 1st student's id: ").strip()
            if UID == "" or len(UID) != 10 or UID[0] == "0" or not UID.isdigit():
                print("Invalid input...\n")
                continue
            else:
                students_info["uid"] = UID
            break
        while True:
            while True:
                Math = int(input("\n""Please insert the 1st student's math score: "))
                if Math < 0:
                    print("Invalid input, The input number must be between 0 and 20")
                    continue
                elif Math > 20:
                    print("Invalid input, The input number must be between 0 and 20")
                    continue
                else:
                    students_info["math"] = Math
                    break
            while True:
                Physics = int(input("Please insert the 1st student's physics score: "))
                if Physics < 0:
                    print("Invalid input, The input number must be between 0 and 20")
                    continue
                elif Physics > 20:
                    print("Invalid input, The input number must be between 0 and 20")
                    continue
                else:
                    students_info["physics"] = Physics
                    break
            while True:
                Chemistry = int(input("Please insert the 1st student's chemistry score: "))
                if Chemistry < 0:
                    print("Invalid input, The input number must be between 0 and 20")
                    continue
                elif Chemistry > 20:
                    print("Invalid input, The input number must be between 0 and 20")
                    continue
                else:
                    students_info["chemistry"] = Chemistry
                    break
            while True:
                E_Language = int(input("Please insert the 1st student's English language score: "))
                if E_Language < 0:
                    print("Invalid input, The input number must be between 0 and 20")
                    continue
                elif E_Language > 20:
                    print("Invalid input, The input number must be between 0 and 20")
                    continue
                else:
                    students_info["elanguage"] = E_Language
                    break
            while True:
                P_Language = int(input("Please insert the 1st student's Persian language score: "))
                if P_Language < 0:
                    print("Invalid input, The input number must be between 0 and 20")
                    continue
                elif P_Language > 20:
                    print("Invalid input, The input number must be between 0 and 20")
                    continue
                else:
                    students_info["planguage"] = P_Language
                    break
            sql_command = """
            INSERT INTO students_info(First_name,Last_name,UID,Math,Physics,Chemistry,E_Language,P_Language)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """
            mycursor.execute(sql_command, tuple(students_info.values()))
            mydb.commit()
            print(mycursor.rowcount, "One students added successfully...\n")
            break
        while True:
            cont = input("To continue this operating press y or no press n: ")
            if cont == "y":
                print("Please wait...\n")
                break
            elif cont == "n":
                print("Thank you for follow this program...")
                exit()
            else:
                print("Invalid input, Please only use y or n...\n")
            continue
        continue


def del_students():
    sql_command = """
    SELECT * FROM students_info
    """
    mycursor.execute(sql_command)
    result = mycursor.fetchall()
    for i in result:
        print(i)
    del_command = input("Please enter student's uid to delete: ")
    sql_command1 = """
    DELETE FROM students_info WHERE uid = %s
    """
    mycursor.execute(sql_command1, int(del_command))
    mydb.commit()
    print("One students has successfully deleted...\n")
    while True:
        while True:
            cont2 = input("To continue this operating press y or no press n: ")
            if cont2 == "y":
                print("Please wait...\n")
                break
            elif cont2 == "n":
                print("Thank you for follow this program...")
                exit()
            else:
                print("Invalid input, Please only use y or n...\n")
            continue
        break


while True:
    msg = input("Please enter an operation to continue (add/delete): ")
    if msg == "add":
        add_students()
    elif msg == "delete":
        del_students()
    else:
        print("Invalid input, Please only use 'yes' or 'no'\n")
        continue
