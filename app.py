import sqlite3

conn = sqlite3.connect("my_database.db")

cursor = conn.cursor()


cursor.execute("""
--begin-sql
CREATE TABLE IF NOT EXISTS product(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    price INTEGER,
    count INTEGER
)

--end-sql
""")

#cursor.execute("SELECT * FROM users")
#all_users = cursor.fetchall()
#for user in all_users:
#    print(user)

cursor.execute("SELECT name, price FROM product WHERE price > 140")
product = cursor.fetchall()
for products in product:
    print(products)

#cursor.execute("UPDATE users SET email = ? WHERE name = ?",("new_leo@mail.ru","leonid"))
#
#
#
#cursor.execute("DELETE FROM users WHERE name = ?",('ivan',))
def add_product(name,price,count):
    try:
        cursor.execute("INSERT INTO product (name,price,count) VALUES (?,?,?)",
                       (name,price,count))
        conn.commit()
    except sqlite3.IntegrityError:
        print("такой товар уже существует, он пропущен")

add_product("oil",150,80)
add_product("batter",300,90)
add_product("rice",40,80)



conn.close()