import sqlite3
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.hashers import make_password
from datetime import datetime

def create_connection(db_file):

    conn = None

    try:
        conn = sqlite3.connect(db_file)
    except:
        print("failed to connect to database")
    
    return conn

def insert(sql):

    conn = create_connection("db.sqlite3")
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def insert(sql, parameters):

    conn = create_connection("db.sqlite3")
    cur = conn.cursor()
    cur.execute(sql, parameters)
    conn.commit()
def select_one(sql):

    conn = create_connection("db.sqlite3")
    cur = conn.cursor()
    cur.execute(sql)
    row = cur.fetchone()

    return row

def select_all(sql):

    conn = create_connection("db.sqlite3")
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()

    return rows

# Flaw 6. Exempts csrf
# Solution: Don't exempt it. Remove @csrf_exempt
@csrf_exempt
def register_user(username, password1, password2, status):
    
    password = check_password(password1, password2)

    if not password:
        return False

    if status == "admin":
        status = True

    else:
        status = False
    # Flaw 1, SQL-injection. The user input values should be parameterized. See solution below.
    sql = f"INSERT INTO bank_account (username, password, admin) VALUES ('{username}', '{password}', {status})"

    # Flaw 1 Solution
    # parameters = [username, password1, status]
    # sql = f"INSERT INTO bank_account (username, password, admin) VALUES (?, ?, ?)"
    # insert2(sql, parameters) 
    # see function "insert2" which uses the parameters correctly.

    insert(sql)

def check_password(password1, password2):

    if password1 != password2:
        return False
    
    # Flaw 2, Identification and Authentication Failures. 
    # This function should do some quality testing on the password
    # but it doesn't. It simply check that they match.

    # SOLUTION:
    # use django's own "make_password function to encrypt password"
    # password = make_password(password1)
    # return password
    # This way passwords aren't stored in plain text in the database.

    password = password1
    
    return password

def get_account(username, password):
    # Another example of flaw 1 where the query should be paramterized to prevent SQL-injection.
    sql = f"SELECT * FROM bank_account WHERE username={username} AND password={password}"
    user = select_one(sql)
    if user == None:
        return False

    # Solution to flaw 3
    # info = {username:username, query:sql}
    # document_to_log(info)

    return user

def get_all_accounts():

    sql = "SELECT * FROM bank_account"
    accounts = select_all(sql)

    return accounts

# Flaw 3. Security Logging and Monitoring Failures.
# Solution to Flaw 3: 
# Function "document_to_log" should be used to document activity across the sight in certain situations.
# Examples where it should be used: "get_account"
def document_to_log(info):
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M:%S")
    log = f"{dt}, Username: {info['username']}, Query: {info['query']}\n"
    with open('log.txt', 'a') as f:
        f.write(log)