#pip install mysql-connector-python

import mysql.connector as connector

class DBHlper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     user='root',
                                     password='root',
                                     database='python31')
        query = 'create table if not exists user_connection(userId int primary key , username varchar(200),phone varchar(10))'
        cur = self.con.cursor()
        cur.execute(query)
        print('created')

    # insert
    def insert_user(self, user_id, user_name, user_phone):
        query = "insert into user_connection(userId,username,phone)values({},'{}','{}')".format(user_id, user_name,
                                                                                                user_phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('user save to db')

    # fech all
    def fech_user(self):
        query = "select * from  user_connection"
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)
            print("User_Id:", row[0])
            print("User_Name:", row[1])
            print("User_Phone:", row[2])
            print()
            print()

    def delete_user(self, userId):
        query = "delete from  user_connection where userId={}".format(userId)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")

    # update
    def update_user(self, userId, new_name, new_phone):
        query = "update user_connection set username='{}',phone='{}' where  userId={}".format(new_name, new_phone,
                                                                                              userId)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('Updated')
