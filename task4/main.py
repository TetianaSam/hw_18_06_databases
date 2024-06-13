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
            colour TEXT,
            calorieContent INTEGER,
            shortDescription TEXT)""")

#cur.execute("""INSERT INTO users (name, age) VALUES ('Jan', 33)""")
#cur.execute("""INSERT INTO users (name, age) VALUES (?, ?)""", ("Adam", 23))
cur.execute("""INSERT INTO veg_fruit (name, type, colour, calorieContent, shortDescription) VALUES (?, ?, ?, ?, ?)""",('apple', 'fruit', 'red', 55, 'worldwide popular fruit'))

#db_insert(cur, "veg_fruit",["name", "type", "colour", "calorie content", "short description"],["apple", "fruit", "red", 54, "worldwide popular fruit"])

conn.commit()

cur.execute("SELECT * FROM veg_fruit")
rows = cur.fetchall()
print(rows)
print("-------")
for row in rows:
   print(row[1],row[2])

conn.close()