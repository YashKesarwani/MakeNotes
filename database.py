import sqlite3
import bcrypt

try:
    conn=sqlite3.connect("UserMaster.db")
    print("Successfully Opened db")
    curr=conn.cursor()
except:
    print("Connection Failed")

def createTable():
    create_table = """CREATE TABLE IF NOT EXISTS cred(id Integer PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL ); """
    curr.execute(create_table)
    conn.commit()
    
def insertData(data):
    insert_data=""" INSERT INTO cred(username,password) VALUES(?,?); """
    curr.execute(insert_data,data)
    conn.commit()
    
def searchData(data):
    search_data=""" SELECT * FROM cred WHERE username=(?); """
    curr.execute(search_data,data)
    rows=curr.fetchall()
    if rows==[]:
        return 1
    return 0
    
def validateData(data,inputData):
    validate_data=""" SELECT * FROM cred WHERE username=(?);"""
    curr.execute(validate_data,data)
    row=curr.fetchall()
    if row[0][1]==inputData[0]:
        return row[0][2]==bcrypt.hashpw(inputData[1].encode(),row[0][2])
    