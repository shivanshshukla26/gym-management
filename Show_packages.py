import mysql.connector as sqltor
import pandas as pd

con=sqltor.connect(host="localhost",user="root",password="Bh00lgaya")
cur=con.cursor()

cur = con.cursor(buffered=True) 
cur.execute("use GYM;")

def Show_packages():
    cur.execute("select * from Packages")
    tableData = cur.fetchall()
    data = pd.DataFrame(tableData)
    data = data.rename(columns={0:"PKname", 1:"Price"})
    return data

