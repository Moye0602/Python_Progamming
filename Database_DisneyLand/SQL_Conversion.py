import pyodbc

# Specify the Microsoft Access database file path
#db_path=
db_path=('\\').join(__file__.split('\\')[:-1])+'\\'

# Connect to the Microsoft Access database
conn_str = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={db_path};'
conn = pyodbc.connect(conn_str)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id AUTOINCREMENT PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
