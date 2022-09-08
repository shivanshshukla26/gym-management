from getpass import getpass
import Add_customer
import Add_packages
import Payment
import Payment
import Show_packages
import Show_cutomers
import datetime

val = 0
print(" ~ Welcome Administrator ~ ")
while val!=1:

    passval = getpass()

    if passval == "Hello":
        print()
        print("Successfull")
        val = 1
    else:
        print()
        print("!! Wrong password. Enter again !!")


exit = 0

def menu():
    print()
    print ("1. Add Customer")#DONE
    print ("2. Add packages")#DONE
    print ("3. Add payment")#DONE
    print ("4. All packages")#DONE
    print ("5. All customers")#DONE
    print ("6. Search customer")#DONE
    print ("7. Cancel subscription")#DONE
    print ("8. Exit")
    print()
    
    
#While loop for menu
while exit!=1:
    menu()

    option = int(input("Enter your choice : "))

    if option == 1:
        print()
        print("--YOU HAVE SELECTED TO ADD CUSTOMER--")
        print()

        #Ask first name
        print()
        Fname = str(input("Enter first name : "))
        print()

        #Ask middle name exists or not
        AskMname = str(input("Does cutomer has middle name (Y/N): "))
        if AskMname == ("Y") or AskMname == ("y"): 
            Mname = str(input("Enter middle name : "))
        else:
            Mname = None

        #Ask last name exists or not
        print()
        AskLname = str(input("Does customer has last name (Y/N): "))
        if AskLname == "Y" or AskLname == "y":
            Lname = str(input("Enter last name : "))
        else:
            Lname = None
        
        #Ask for phone number
        print()
        phone = Add_customer.Phone_validation()
        print()

        #Validation for existence
        check = Add_customer.Insert.check(Fname, phone)
        if check == True:
            pass
        else:
            print("!! CUSTOMER ALREADY EXISTS !! ")
            continue

        #Ask for type of Proof of identity
        print()
        print("Type of proof of identity accepted : ")
        print("1. Adhaar card (AC)")
        print("2. Pan card (PC)")
        print("3. Voter ID (VI)")
        print("4. Driving license (DL)")
        print()

        POItype = str(input("Enter type of POI : "))                
        print()

        POInum = str(input("Enter POI number : "))
        print()

        #Ask for package details
        print(Show_packages.Show_packages())
        print()
        while True:
            package = str(input("Enter package name : "))
            if Add_customer.Package_validation(package) == True:
                break
            else:
                print("!! Enter package name correctly !!")
                print()
        print()

        #print payment
        last_payment = datetime.date.today().strftime("%d/%m/%y")
        next_payment = datetime.date.today() + datetime.timedelta(days=28)
        next_payment = next_payment.strftime("%d/%m/%Y")
        print("~ ~ Congratulations!! Your subscription starts from today ~ ~")
        print()


        Add_customer.Insert(Fname,Mname,Lname,POInum,POItype,phone, package,last_payment,next_payment)



#Option to create new package
    if option == 2:
        print()
        print(" --YOU HAVE SELECTED TO ADD PACKAGE-- ")
        print()
        print()
        PKname = str(input("Enter package name : "))
        print()
        price = int(input("Enter Price of package : "))
        print()
        print("New package name : ",PKname," ","Price : ",price)
        Add_packages.add_Package(PKname, price)
        #module complete



#Option to add payment
    if option == 3:
        print()
        print(" --YOU HAVE SELECTED TO ADD PAYMENT-- ")
        print()
        print()
        fname = str(input("Enter name to search : "))
        print()
        phone = str(input("Enter phone to search : "))
        print()
        payment_date = Payment.payment(fname,phone)
        today = datetime.date.today()
        today = today.strftime("%d/%m/%y")  
        if payment_date == today:
            print("Your payment is due today ")
        else:
            print("Your payment is due on ", payment_date)



#Option to show packages
    if option == 4:
        print()
        print(" --YOU HAVE SELECTED TO SHOW PACKAGES-- ")
        print()
        print()
        print(Show_packages.Show_packages())
        #module complete



#Show all customers
    if option == 5:
        print()
        print(" --YOU HAVE SELECTED TO SHOW ALL CUSTOMERS-- ")
        print()
        print()
        print(Show_cutomers.show_all_customer())
        #Module complete



#Search a customer
    if option == 6:
        print()
        print(" --YOU HAVE SELECTED TO SEARCH CUSTOMER-- ")
        print()
        print()
        searchFname = str(input("Enter Fname for searching : "))
        print()
        searchPhone = int(input("Enter phone for searching : "))
        print()
        print(Show_cutomers.search_customer(searchFname, searchPhone))
        #Module complete



#option to cancel subscription
    if option == 7:
        print()
        print(" --YOU HAVE SELECTED TO CANCEL SUBSCRIPTION-- ")
        print()
        print()
        Fname = str(input("Enter first name : "))
        phone = int(input("Enter phone number : "))
        Payment.cancel(Fname,phone)
        print()
        print("!! YOUR SUBSCRIPTION HAS BEEN CANCELED !!")


#option to exit
    if option == 8:
        exit = 1