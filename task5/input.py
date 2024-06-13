def display_menu():
    print("""
    _____________MENU_____________
    [1] - Displaying of all data from the table about vegetables and fruit.
    [2] - Displaying of all vegetables.
    [3] - Displaying of all fruit.
    [4] - Displaying of all the names of vegetables and fruit.
    [5] - Displaying of all colors. Colors should be unique.
    [6] - Displaying fruit of a specific color.
    [7] - Displaying vegetables of a particular color
    [8] - Finish
    """)

def user_input():
    user_choice = int(input("Enter your choice: ")
    if user_choice  == 1:
        cur.execute("SELECT * FROM veg_fruit")
        rows = cur.fetchall()
        print(rows)
        print("-------")
        for row in rows:
            print(row[1], row[2])
    if user_choice == 2:
        cur.execute("SELECT type FROM veg_fruit where type = 'vegetable'")
        rows = cur.fetchall()
        print(rows)
        print("-------")
        for row in rows:
            print(row[1], row[2])
    if user_choice == 3:
        cur.execute("SELECT type FROM veg_fruit where type = 'fruit'")
        rows = cur.fetchall()
        print(rows)
        print("-------")
        for row in rows:
            print(row[1], row[2])

    if user_choice == 4:
        cur.execute("SELECT name FROM veg_fruit ")
        rows = cur.fetchall()
        print(rows)
        print("-------")
        for row in rows:
            print(row[1], row[2])

    if user_choice == 5:
        cur.execute("SELECT DISTINCT color FROM veg_fruit")
        rows = cur.fetchall()
        print(rows)
        print("-------")
        for row in rows:
            print(row[1], row[2])