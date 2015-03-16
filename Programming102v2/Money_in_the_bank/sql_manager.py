import requests
import sqlite3
from Client import Client


class BankDB():

    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    @staticmethod
    def create_clients_table():
        create_query = '''create table if not exists
            clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    password TEXT,
                    balance REAL DEFAULT 0 CHECK(balance>=0),
                    message TEXT,
                    email TEXT)'''
        BankDB.cursor.execute(create_query)

    def change_message(new_message, logged_user):
        BankDB.cursor.execute("UPDATE clients SET message = ? WHERE id = ?",
                              (new_message, logged_user.get_id()))
        BankDB.conn.commit()
        logged_user.set_message(new_message)

    def make_transaction(amount, logged_user):

        BankDB.cursor.execute("UPDATE clients SET balance = ? WHERE id = ?",
                              (amount, logged_user.get_id()))
        BankDB.conn.commit()

    def change_pass(new_pass, logged_user):
        BankDB.cursor.execute("UPDATE clients SET password = '%s' WHERE id = '%s'" % (
            new_pass, logged_user.get_id()))
        BankDB.conn.commit()

    def change_email(new_email, logged_user):
        BankDB.cursor.execute("UPDATE clients SET email = '%s' WHERE id = '%s'" % (
            new_email, logged_user.get_id()))
        BankDB.conn.commit()

    def register(username, password):
        BankDB.cursor.execute(
            '''INSERT INTO clients (username, password) values (?,?)''', (username, password))
        BankDB.conn.commit()

    def login(username, password):
        BankDB.cursor.execute(
            "SELECT id, username, balance, message FROM clients WHERE username = ? AND password = ? LIMIT 1", (username, password))
        user = BankDB.cursor.fetchone()
        if(user):
            return Client(user[0], user[1], user[2], user[3])
        else:
            return False


