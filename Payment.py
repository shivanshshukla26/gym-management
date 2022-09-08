import mysql.connector as sqltor
from datetime import datetime


con=sqltor.connect(host="localhost",user="root",password="Bh00lgaya")
cur=con.cursor()

cur = con.cursor(buffered=True) 
cur.execute("use GYM;")

def payment(fname, phone):
    cur.execute("select next_payment from member where Fname = (%s) and phone = (%s)",(fname, phone, ))
    data = cur.fetchone()
    for row in data:
        data = row
    return data


def cancel(fname, phone):
    cur.execute("delete from member where Fname = (%s) and phone = (%s)", (fname, phone,))
    con.commit()