import mysql.connector as sqltor
import pandas as pd

con=sqltor.connect(host="localhost",user="root",password="Bh00lgaya")
cur=con.cursor()

cur = con.cursor(buffered=True) 
cur.execute("use GYM;")

def show_all_customer():
    cur.execute("select * from member")
    tableData = cur.fetchall()
    data = pd.DataFrame(tableData)
    data = data.rename(columns={0:"Fname", 1:"Mname", 2:"Lname", 3:"POI", 4:"POItype", 5:"Phone", 6:"package"})
    return data

def search_customer(fname, phone):
    cur.execute("select * from member where fname = (%s) and phone = (%s)",(fname, phone,))
    tableData = cur.fetchall()
    data = pd.DataFrame(tableData)
    data = data.rename(columns={0:"Fname", 1:"Mname", 2:"Lname", 3:"POI", 4:"POItype", 5:"Phone", 6:"package"})
    return data