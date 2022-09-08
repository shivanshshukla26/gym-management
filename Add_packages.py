import mysql.connector as sqltor
con=sqltor.connect(host="localhost",user="root",password="Bh00lgaya")
cur=con.cursor()

cur = con.cursor(buffered=True) 
cur.execute("use GYM;")
cur.execute("create table if not exists Packages"
            "("
            "PKname varchar(20) not null,"
            "Price char(10)"
            ")")

class add_Package:
    def __init__(self, PKname, price):
        self.PKname = PKname
        self.price = price
        cur.execute("insert into Packages values(%s ,%s)",(self.PKname, self.price,))
        
        con.commit()

