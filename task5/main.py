import sqlite3


def db_insert(db_cur, table, cols, vals):
   # check table
   if len(cols) != len(vals):
      return False

   columns = " "
   for item in cols:
      columns += f"{item},"


   values = " "
   for item in range(len(vals)):
      values += "?,"

   try:
      query = f"""INSERT INTO {table} ({columns[:-1]}) VALUES ({values[:-1]})"""
      db_cur.execute(query, vals)
   except:
      return False

   return True

conn = sqlite3.connect("task4_veg_fruit_db.db")

cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS veg_fruit (
            id INTEGER PRIMARY KEY,
            name TEXT,
            type TEXT,
            color TEXT,
            calorieContent INTEGER,
            shortDescription TEXT)""")
cur.execute("""INSERT INTO veg_fruit (name, type, color,calorieContent,shortDescription) VALUES (?, ?, ?, ?, ?)""", ("apple", "fruit","Red", 55, "worldwide fruit"))

if db_insert(cur, "veg_fruit", ["name", "type", "color", "calorieContent", "shortDescription"],
             ["Apple", "Fruit", "green", 56, "worldwide popular fruit"]):
    print("Record inserted successfully.")
else:
    print("Failed to insert record.")


conn.commit()


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
    while True:
        display_menu()
        try:
            user_choice = int(input("Enter your choice: "))

            if user_choice == 1:
                cur.execute("SELECT * FROM veg_fruit")
                rows = cur.fetchall()
                print(rows)
                print("All records:")
                for row in rows:
                    print(row[:6])

            elif user_choice == 2:
                cur.execute("SELECT  * FROM veg_fruit where type = 'vegetable';")
                rows = cur.fetchall()
                print(rows)
                print("All vegetables:")
                for row in rows:
                    print(row[:6])

            elif user_choice == 3:
                cur.execute("SELECT name FROM veg_fruit where type = 'fruit';")
                rows = cur.fetchall()
                print(rows)
                print("All fruits:")
                for row in rows:
                    print(row[0:5])

            elif user_choice == 4:
                cur.execute("SELECT name FROM veg_fruit ")
                rows = cur.fetchall()
                print(rows)
                print("All names:")
                for row in rows:
                    print(row[0:5])

            elif user_choice == 5:
                cur.execute("SELECT DISTINCT color FROM veg_fruit")
                rows = cur.fetchall()
                print(rows)
                print("All unique colors:")
                for row in rows:
                    print(row[0:6])

            elif user_choice == 6:
                color = input("Enter the color: ")
                cur.execute("SELECT * FROM veg_fruit WHERE type = 'fruit' AND color = ?", (color,))
                rows = cur.fetchall()
                print(f"All fruits of color {color}:")
                for row in rows:
                    print(row)
                print("-------")

            elif user_choice == 7:
                color = input("Enter the color: ")
                cur.execute("SELECT * FROM veg_fruit WHERE type = 'vegetable' AND color = ?", (color,))
                rows = cur.fetchall()
                print(f"All vegetables of color {color}:")
                for row in rows:
                    print(row)
                print("-------")

            elif user_choice == 8:
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 8.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")




user_input()
conn.close()