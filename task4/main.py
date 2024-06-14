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
            calorie content INTEGER,
            short description TEXT)""")
if db_insert(cur, "veg_fruit", ["name", "type", "color", "calorie_content", "short_description"],
             ["apple", "fruit", "red", 55, "worldwide popular fruit"]):
    print("Record inserted successfully.")
else:
    print("Failed to insert record.")


conn.commit()

cur.execute("SELECT * FROM veg_fruit")
rows = cur.fetchall()
print(rows)
print("All records:")
for row in rows:
   print(row[:6])

conn.close()