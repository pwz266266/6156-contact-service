import pymysql

import os


class ContactResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        usr = os.environ.get("DBUSER")
        pw = os.environ.get("DBPW")
        h = os.environ.get("DBHOST")

        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def _execute_sql(sql, args):
        conn = ContactResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=args)
        result = cur.fetchone()

        return result

    @staticmethod
    def get_email_by_id(id):
        sql = "SELECT * FROM Contacts.Email where user_id=%s";
        return ContactResource._execute_sql(sql, id)

    @staticmethod
    def delete_email_by_id(id):
        sql = "DELETE FROM Contacts.Email where user_id=%s";
        return ContactResource._execute_sql(sql, id)

    @staticmethod
    def update_email_by_id(id, email):
        sql = "UPDATE Contacts.Email SET email=%s where user_id=%s";
        return ContactResource._execute_sql(sql, [email, id])

    @staticmethod
    def insert_email_by_id(id, email):
        sql = "INSERT INTO Contacts.Email VALUES (%s, %s)";
        return ContactResource._execute_sql(sql, [id, email])


    @staticmethod
    def get_address_by_id(id):
        sql = "SELECT * FROM Contacts.Address where user_id=%s";
        return ContactResource._execute_sql(sql, id)
    
    @staticmethod
    def delete_address_by_id(id):
        sql = "DELETE FROM Contacts.Address where user_id=%s";
        return ContactResource._execute_sql(sql, id)

    @staticmethod
    def update_address_by_id(id, address):
        sql = "UPDATE Contacts.Address SET address=%s where user_id=%s";
        return ContactResource._execute_sql(sql, [address, id])

    @staticmethod
    def insert_address_by_id(id, address):
        sql = "INSERT INTO Contacts.Address VALUES (%s, %s)";
        return ContactResource._execute_sql(sql, [id, address])

    @staticmethod
    def get_phone_by_id(id):
        sql = "SELECT * FROM Contacts.Phone where user_id=%s";
        return ContactResource._execute_sql(sql, id)

    @staticmethod
    def delete_phone_by_id(id):
        sql = "DELETE FROM Contacts.Phone where user_id=%s";
        return ContactResource._execute_sql(sql, id)

    @staticmethod
    def update_phone_by_id(id, phone):
        sql = "UPDATE Contacts.Phone SET phone=%s where user_id=%s";
        return ContactResource._execute_sql(sql, [phone, id])

    @staticmethod
    def insert_phone_by_id(id, phone):
        sql = "INSERT INTO Contacts.Phone VALUES (%s, %s)";
        return ContactResource._execute_sql(sql, [id, phone])