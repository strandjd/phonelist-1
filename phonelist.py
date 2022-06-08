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
def add_phone(C, name, phone, address):
    cur = C.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}', '{address}');")
    cur.close()
def delete_phone(C, id):
    cur = C.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE id = '{id}';")
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
    '\n',
    ' ADD:      Add a name to the list',
    ' LIST:     Print the list of names',
    ' SAVE:     Save phonelist',
    ' DELETE:   Delete phone',
    ' QUIT:     End the program by pressing ctrl +c',
    ' HELP:     Command list options\n']



for x in commands:
    print(x)




while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ").strip().upper()
    if cmd == "LIST":
        print(read_phonelist(conn))
    elif cmd == "ADD":
        name = input("  Name: ").strip().title()
        address = input("  Address: ").strip().title()
        phone = input("  Phone: ").strip()
        add_phone(conn, name, address, phone)
    elif cmd == "DELETE":
        id = input("  ID: ").strip()
        delete_phone(conn, id)
    elif cmd == "SAVE":
        save_phonelist(conn)
    elif cmd == "QUIT":
        save_phonelist(conn)
        exit()
    elif cmd == "HELP":
        for x in commands:
            print(x)
    else:
        print('\nInvalid command. Try again.\n')
        for x in commands:
            print(x)
