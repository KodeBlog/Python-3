from mysql.connector import connect

connection = connect(host='localhost',database='python_db',user='jk',password='.Melody2019',auth_plugin='mysql_native_password')

print('Attempting to connect to the database...')
if connection.is_connected():
    print("Connection to the database established successfully")

def display_all_users():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users;")
    records = cursor.fetchall()

    heading = f"Total registered users in the system: {cursor.rowcount}"
    print(heading)
    print ("-" * len(heading))
    for row in records:
        print(f"ID: {row[0]}")
        print(f"Username: {row[1]}")
        print(f"Email: {row[2]}")
        print(f"Created At: {row[4]}\n")
    
    cursor.close()
    connection.close()
    print("MySQL connection is closed")

def add_new_user(user):
    sql_stmt = """INSERT INTO users (username,email,password) VALUES (%s,%s,%s)"""
    
    cursor = connection.cursor(prepared=True)
    cursor.execute(sql_stmt,user)
    connection.commit()
    cursor.close()
    connection.close()

    print("Record successfully inserted into the database using prepared stament")


def search_users(query):
    sql_stmt = f"SELECT * FROM users WHERE username LIKE '%{query}%' OR email LIKE '%{query}%'"

    cursor = connection.cursor()
    cursor.execute(sql_stmt)
    records = cursor.fetchall()

    heading = f"search for '{query}' returned: {cursor.rowcount} rows"
    print(heading)
    print ("-" * len(heading))
    for row in records:
        print(f"ID: {row[0]}")
        print(f"Username: {row[1]}")
        print(f"Email: {row[2]}")
        print(f"Created At: {row[4]}\n")
    
    cursor.close()
    connection.close()
    print("MySQL connection is closed")


def update_user(user):
    sql_stmt = "UPDATE users SET updated_at = NOW(), username = %s,email = %s,password = %s WHERE id = %s"

    cursor = connection.cursor(prepared=True)
    cursor.execute(sql_stmt,user)
    connection.commit()
    cursor.close()
    connection.close()

    print("Record successfully updated in the database using prepared stament")

def delete_user(id):
    sql_stmt = "DELETE FROM users WHERE id = %s"
    param = (id)
    cursor = connection.cursor(prepared=True)
    cursor.execute(sql_stmt,param)
    connection.commit()
    cursor.close()
    connection.close()

    print("Record successfully deleted from the database using prepared stament")