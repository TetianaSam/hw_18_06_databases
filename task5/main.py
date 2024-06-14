import sqlite3


def db_insert(db_cur, table, cols, vals):
   # check table
   if len(cols) != len(vals):
      return False

   columns = " "
   for item in cols:
      columns += f"{item},"

   """
   values = ""
   for item in vals:
      values += f"'{item}',"
   """

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

#cur.execute("""INSERT INTO users (name, age) VALUES ('Jan', 33)""")
#cur.execute("""INSERT INTO users (name, age) VALUES (?, ?)""", ("Adam", 23))
cur.execute("""INSERT INTO veg_fruit (name, type, color, calorieContent, shortDescription) VALUES (?, ?, ?, ?, ?)""",
            ('potato','vegetable','white',90,'popular vegetable'))
cur.execute("""INSERT INTO veg_fruit (name, type, color, calorieContent, shortDescription) VALUES (?, ?, ?, ?, ?)""",
            ('apple','fruit','yellow',40,'popular vegetable'))
#db_insert(cur, "veg_fruit",["name", "type", "colour", "calorie content", "short description"],["apple", "fruit", "red", 54, "worldwide popular fruit"])

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

    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        cur.execute("SELECT * FROM veg_fruit")
        rows = cur.fetchall()
        print(rows)
        print("-------")
        for row in rows:
            print(row[:6])

    if user_choice == 2:
        cur.execute("SELECT  * FROM veg_fruit where type = 'vegetable';")
        rows = cur.fetchall()
        print(rows)
        print("-------")
        for row in rows:
            print(row[:6])

    if user_choice == 3:
        cur.execute("SELECT name FROM veg_fruit where type = 'fruit';")
        rows = cur.fetchall()
        print(rows)
        print("-------")
        for row in rows:
            print(row[0:5])

    if user_choice == 4:
        cur.execute("SELECT name FROM veg_fruit ")
        rows = cur.fetchall()
        print(rows)
        print("-------")
        for row in rows:
            print(row[0:5])

    if user_choice == 5:
        cur.execute("SELECT DISTINCT color FROM veg_fruit")
        rows = cur.fetchall()
        print(rows)
        print("-------")
        for row in rows:
            print(row[0:5])
    if user_choice == 6:
        cur.execute("SELECT DISTINCT * FROM veg_fruit where type = 'fruit' and color = 'yellow'")
        rows = cur.fetchall()
        print(rows)
        print("-------")
        for row in rows:
            print(row[:6])
    if user_choice == 7:
        cur.execute("SELECT DISTINCT * FROM veg_fruit where type = 'vegetable' and color = 'red'")
        rows = cur.fetchall()
        print(rows)
        print("-------")
        for row in rows:
            print(row[:6])


display_menu()
user_input()
conn.close()