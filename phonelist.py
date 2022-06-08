#import sqlite3
#conn = sqlite3.connect("phone.db")

import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="phone",
    user="phone",
    password="abc123"
    )


def read_phonelist(C):
    cur = C.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_phone(C, name, phone):
    cur = C.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}');")
    cur.close()
def delete_phone(C, name):
    cur = C.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE name = '{name}';")
    cur.close()
def save_phonelist(C):
    cur = C.cursor()
    try:
        cur.execute("COMMIT;")
    except:
        print("No changes!")
    cur.close()

print("-----Hello and welcome to The List-----")

commands = [
    'ADD: Add a name to the list',
    'LIST: Print the list of names',
    'QUIT: End the program by pressing ctrl +c']



for x in commands:
    print(x)




while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ").strip().upper()
    if cmd == "LIST":
        print(read_phonelist(conn))
    elif cmd == "ADD":
        name = input("  Name: ").strip().title()
        phone = input("  Phone: ").strip()
        add_phone(conn, name, phone)
    elif cmd == "DELETE":
        name = input("  Name: ").strip().title()
        delete_phone(conn, name)
    elif cmd == "QUIT":
        save_phonelist(conn)
        exit()
    else:
        print('\nInvalid command. Try again.\n')
        for x in commands:
            print(x)
    print('Bye, see you L8R!')
