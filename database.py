import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="company"
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query, values=None):
    cursor = connection.cursor()
    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def fetch_query(connection, query, values=None):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
    except Error as e:
        print(f"The error '{e}' occurred")
    return result

def create_employee(connection, name, dept, role):
    query = "INSERT INTO company (name, dept, role) VALUES (%s, %s, %s)"
    values = (name, dept, role)
    execute_query(connection, query, values)

def get_employees(connection):
    query = "SELECT * FROM company"
    return fetch_query(connection, query)

def get_employee_by_id(connection, employee_id):
    query = "SELECT * FROM company WHERE id = %s"
    values = (employee_id,)
    return fetch_query(connection, query, values)

def update_employee(connection, employee_id, name, dept, role):
    query = "UPDATE company SET name = %s, dept = %s, role = %s WHERE id = %s"
    values = (name, dept, role, employee_id)
    execute_query(connection, query, values)

def delete_employee(connection, employee_id):
    query = "DELETE FROM company WHERE id = %s"
    values = (employee_id,)
    execute_query(connection, query, values)
