#customer details 
from datetime import datetime
from dateutil.relativedelta import relativedelta

import mysql.connector as sqltor
con=sqltor.connect(host="localhost",user="root",password="Bh00lgaya")
cur=con.cursor()

cur = con.cursor(buffered=True) 
cur.execute("use GYM;")

cur.execute("create table if not exists member"
            "("
            "Fname varchar(50) not null, "
            "Mname varchar(50), "
            "Lname varchar(50), "
            "POI varchar(20) not null,"
            "POItype varchar(5) not null,"
            "phone bigint(10) not null, "
            "package varchar(20) not null,"
            "last_payment varchar(20) not null,"
            "next_payment varchar(20) not null"
            ")")

#class for name
class Insert:
    def __init__(self,Fname,Mname,Lname, POInum, POItype, Number, selectPackage, last_payment, next_payment):
        self.Fname = Fname
        self.Mname = Mname
        self.Lname = Lname
        self.POInum = POInum
        self.POItype = POItype
        self.Number = Number
        self.selectPackage = selectPackage
        self.last_payment = last_payment
        self.next_payment = next_payment
        cur.execute("insert into member values(%s,%s,%s,%s,%s,%s,%s, %s, %s)",(self.Fname, self.Mname, self.Lname, self.POInum, self.POItype, self.Number, self.selectPackage, self.last_payment, self.next_payment))

        con.commit()

    def check(fname, phone):
        cur.execute("select * from member where fname = (%s) and phone = (%s)",(fname, phone))
        data = cur.fetchall()
        if len(data) == 0:
            return True
        else:
            return False



def Phone_validation():
    while True:
        phone = input("Enter phone number : ")
        if phone.isdigit() == True and len(phone) == 10:
            return phone
        else:
            print("!! Enter 10 digits !!")

def Package_validation(package):
    cur.execute("select * from packages where PKname = (%s)",(package,))
    data = cur.fetchall()
    if len(data) == 0:
        return False
    else:
        return True


